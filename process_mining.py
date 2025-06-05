import pm4py

def compute_heuristic():
    log = pm4py.read_xes("event_log.xes")

    heu_net = pm4py.discover_heuristics_net(log) # Apply the algorithm.

    net, im, fm = pm4py.convert_to_petri_net(heu_net)

    # Visualise the Petri net with annotations
    parameters = {pm4py.visualization.petri_net.visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
    gviz = pm4py.visualization.petri_net.visualizer.apply(net, im, fm, parameters=parameters)

    pm4py.visualization.petri_net.visualizer.save(gviz, "heuristic.png")

    fitness = pm4py.algo.evaluation.replay_fitness.algorithm.apply(log, net, im, fm)
    print("Fitness in heuristic miner:", fitness)

def compute_alpha():
    log = pm4py.read_xes("event_log.xes")

    net, im, fm = pm4py.discover_petri_net_alpha(log) # Apply the algorithm.

    parameters = {pm4py.visualization.petri_net.visualizer.Variants.FREQUENCY.value.Parameters.FORMAT: "png"}
    gviz = pm4py.visualization.petri_net.visualizer.apply(net, im, fm, parameters=parameters)

    pm4py.visualization.petri_net.visualizer.save(gviz, "alpha.png")

    fitness = pm4py.algo.evaluation.replay_fitness.algorithm.apply(log, net, im, fm)
    print("Fitness in alpha miner:", fitness)

if __name__ == "__main__":
    compute_heuristic()
    compute_alpha()
