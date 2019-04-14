import json
import os
import time
import numpy as np

from .base import BaseExperiment, OUTPUT_DIRECTORY

import solvers

if not os.path.exists(OUTPUT_DIRECTORY + '/Q'):
    os.makedirs(OUTPUT_DIRECTORY + '/Q')
if not os.path.exists(OUTPUT_DIRECTORY + '/Q/pkl'):
    os.makedirs(OUTPUT_DIRECTORY + '/Q/pkl')
if not os.path.exists(OUTPUT_DIRECTORY + '/images/Q'):
    os.makedirs(OUTPUT_DIRECTORY + '/images/Q')


class QLearnerExperiment(BaseExperiment):
    def __init__(self, details, verbose=False):
        self.max_episodes = 2500

        super(QLearnerExperiment, self).__init__(details, verbose)

    def convergence_check_fn(self, solver, step_count):
        return solver.has_converged()

    def perform(self):
        # Q-Learner
        self._details.env.reset()
        map_desc = self._details.env.unwrapped.desc

        grid_file_name = '{}/Q/{}_grid.csv'.format(OUTPUT_DIRECTORY, self._details.env_name)
        with open(grid_file_name, 'w') as f:
            f.write("params,time,steps,reward_mean,reward_median,reward_min,reward_max,reward_std\n")

        alphas = [1.0]  # [1.0]
        alpha_decays = [0.001]  # [0.01, 0.001]
        alpha_mins = [0.1]
        q_inits = [0]  # [0, 1.0, 'random']
        epsilons = [0, 0.1, 0.5, 0.9, 1.0]  # [1.0]
        epsilon_decays = [0.0]  # [0.001]
        epsilon_mins = [0.0]  # [0.1]
        # discount_factors = np.round(np.linspace(0, 0.9, num=10), 2)
        discount_factors = [0.9]
        dims = len(discount_factors) * len(alphas) * len(q_inits) * len(epsilons) * len(epsilon_decays)
        self.log("Searching Q in {} dimensions".format(dims))

        runs = 1
        for alpha in alphas:
            for alpha_decay in alpha_decays:
                for alpha_min in alpha_mins:
                    for q_init in q_inits:
                        for epsilon in epsilons:
                            for epsilon_decay in epsilon_decays:
                                for epsilon_min in epsilon_mins:
                                    for discount_factor in discount_factors:
                                        t = time.clock()
                                        self.log("{}/{} Processing Q with alpha {}, q_init {}, epsilon {}, epsilon_decay {},"
                                                 " discount_factor {}".format(
                                            runs, dims, alpha, q_init, epsilon, epsilon_decay, discount_factor
                                        ))

                                        qs = solvers.QLearningSolver(self._details.env, self.max_episodes,
                                                                     discount_factor=discount_factor,
                                                                     alpha=alpha, alpha_decay=alpha_decay, alpha_min=alpha_min,
                                                                     epsilon=epsilon, epsilon_decay=epsilon_decay, epsilon_min=epsilon_min,
                                                                     q_init=q_init, verbose=self._verbose)

                                        stats = self.run_solver_and_collect(qs, self.convergence_check_fn)

                                        self.log("Took {} episodes".format(len(stats.steps)))
                                        stats.to_csv('{}/Q/{}_{}_{}_{}_{}_{}_{}_{}_{}.csv'.format(OUTPUT_DIRECTORY,
                                                                                         self._details.env_name,
                                                                                         alpha, alpha_decay, alpha_min,
                                                                                         q_init,
                                                                                         epsilon, epsilon_decay, epsilon_min,
                                                                                         discount_factor))
                                        stats.pickle_results('{}/Q/pkl/{}_{}_{}_{}_{}_{}_{}_{}_{}_{}.pkl'.format(OUTPUT_DIRECTORY,
                                                                                                        self._details.env_name,
                                                                                                        alpha, alpha_decay, alpha_min,
                                                                                                        q_init,
                                                                                                        epsilon, epsilon_decay, epsilon_min,
                                                                                                        discount_factor,
                                                                                                        '{}'), map_desc.shape,
                                                              step_size=self.max_episodes/20.0)
                                        stats.plot_policies_on_map('{}/images/Q/{}_{}_{}_{}_{}_{}_{}_{}_{}_{}.png'.format(OUTPUT_DIRECTORY,
                                                                                                              self._details.env_name,
                                                                                                              alpha, alpha_decay, alpha_min,
                                                                                                              q_init, epsilon,
                                                                                                              epsilon_decay, epsilon_min,
                                                                                                              discount_factor,
                                                                                                              '{}_{}'),
                                                                   map_desc, self._details.env.colors(),
                                                                   self._details.env.directions(),
                                                                   'Q-Learner', 'Episode', self._details,
                                                                   step_size=self.max_episodes / 20.0,
                                                                   only_last=True)

                                        stats.plot_q_on_map('{}/images/Q/{}_{}_{}_{}_{}_{}_{}_{}_{}_{}.png'.format(OUTPUT_DIRECTORY,
                                                                                                          self._details.env_name,
                                                                                                          alpha, alpha_decay, alpha_min,
                                                                                                          q_init,
                                                                                                          epsilon, epsilon_decay, epsilon_min,
                                                                                                          discount_factor,
                                                                                                          '{}_{}'),
                                                                   map_desc, qs, self._details.env.directions())

                                        # We have extra stats about the episode we might want to look at later
                                        episode_stats = qs.get_stats()
                                        episode_stats.to_csv('{}/Q/{}_{}_{}_{}_{}_{}_{}_{}_{}_episode.csv'.format(OUTPUT_DIRECTORY,
                                                                                                         self._details.env_name,
                                                                                                         alpha, alpha_decay, alpha_min,
                                                                                                         q_init, epsilon,
                                                                                                         epsilon_decay, epsilon_min,
                                                                                                         discount_factor))

                                        optimal_policy_stats = self.run_policy_and_collect(qs, stats.optimal_policy)
                                        self.log('{}'.format(optimal_policy_stats))
                                        optimal_policy_stats.to_csv('{}/Q/{}_{}_{}_{}_{}_{}_{}_{}_{}_optimal.csv'.format(OUTPUT_DIRECTORY,
                                                                                                             self._details.env_name,
                                                                                                             alpha, alpha_decay, alpha_min,
                                                                                                             q_init, epsilon,
                                                                                                             epsilon_decay, epsilon_min,
                                                                                                             discount_factor))

                                        with open(grid_file_name, 'a') as f:
                                            f.write('"{}",{},{},{},{},{},{},{}\n'.format(
                                                json.dumps({
                                                    'alpha': alpha,
                                                    'alpha_decay': alpha_decay,
                                                    'alpha_min': alpha_min,
                                                    'q_init': q_init,
                                                    'epsilon': epsilon,
                                                    'epsilon_decay': epsilon_decay,
                                                    'epsilon_min': epsilon_min,
                                                    'discount_factor': discount_factor,
                                                }).replace('"', '""'),
                                                time.clock() - t,
                                                len(optimal_policy_stats.rewards),
                                                optimal_policy_stats.reward_mean,
                                                optimal_policy_stats.reward_median,
                                                optimal_policy_stats.reward_min,
                                                optimal_policy_stats.reward_max,
                                                optimal_policy_stats.reward_std,
                                            ))
                                        runs += 1