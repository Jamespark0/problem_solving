from itertools import cycle;

def dyanmicMonteCarlo(num_A: int, num_B:int, period:int) -> list:
    # some constants from the problem
    k1 = 0.2
    k2 = 0.2
    step = 2
    _ = [0.800, 0.801, 0.752, 0.661, 0.169, 0.956, 0.949, 0.003, 0.201, 0.291, 0.615, 0.131, 0.241, 0.685, 0.116, 0.241, 0.849];
    randomNumBuffer = iter(cycle(_));

    particle_num: dict = {'A': num_A, 'B': num_B};
    iteration: int = period // 2;

    def pick_random() -> list:
        '''return reactant, rate k, and product'''
        # randomly pick a number between 0 and 1 to decide the probability
        threshold = next(randomNumBuffer);
        if threshold <= particle_num['A']/sum(particle_num.values()):
            return ['A', k1, 'B'];
        return ['B', k2, 'A'];

    for _ in iter(range(iteration * sum(particle_num.values()))):
        reactant, k, product = pick_random();
        if next(randomNumBuffer) < k*step:
            particle_num[reactant] -= 1;
            particle_num[product] += 1;
    
    return particle_num['B'];


if __name__ == "__main__":
    print(dyanmicMonteCarlo(4, 3, 2));