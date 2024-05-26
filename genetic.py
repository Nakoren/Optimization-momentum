import numpy as np

def rosenbrockPlot(x,y):
    return (1 - x) ** 2 + 100*((y - x**2)**2)
# Функция Розенброка
def rosenbrock(x):
    return sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)


# Генетический алгоритм
def genetic_algorithm(pop_size, dim, generations):
    # Инициализация начальной популяции
    population = np.random.uniform(-5, 5, (pop_size, dim))

    for _ in range(generations):
        # Оценка приспособленности особей
        fitness = np.array([rosenbrock(ind) for ind in population])

        # Выбор лучших особей для скрещивания
        selected_indices = np.argsort(fitness)[:pop_size // 2]
        selected_individuals = population[selected_indices]

        # Скрещивание и мутация
        children = []
        for _ in range(pop_size - len(selected_individuals)):
            parent1, parent2 = selected_individuals[np.random.choice(len(selected_individuals), 2, replace=False)]
            crossover_point = np.random.randint(dim)
            child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            mutation_prob = 0.1
            if np.random.rand() < mutation_prob:
                mutation_index = np.random.randint(dim)
                child[mutation_index] += np.random.normal(0, 0.1)
            children.append(child)

        # Обновление популяции
        population = np.vstack((selected_individuals, children))

    # Возвращаем лучшую особь и ее значение функции приспособленности
    best_index = np.argmin(fitness)
    #best_individual = population[best_index]
    best_individual = tuple(population[best_index])
    best_individual_list =[]
    best_individual_list.append(best_individual)
    best_fitness = fitness[best_index]

    return best_individual_list, best_fitness

