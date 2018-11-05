from DE_Assigment.ploting import *

# Costs:
# ______________________________
steps_count = 100
X = 10

glob_err_start = 20
glob_err_end = 1000
# ______________________________


# Plotting graphs for each task:
plot_methods(steps_count, X)
plot_local_error(steps_count, X)
plot_global_error(glob_err_start, glob_err_end, X)
