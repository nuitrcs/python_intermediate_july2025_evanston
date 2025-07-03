# It's your turn to try creating and using virtual environments

1. Create two environments (I provide shell commands below, but if you are working in the Anaconda Navigator you can do this in the Navigator GUI via point-and-click and hand-selecting these packages):

    ```
    conda create --name numpy1-test python=3.12 numpy=1.26.4 jupyter
    ```

    ```
    conda create --name numpy2-test python=3.12 numpy=2.1.2 jupyter
    ```

2.  Download these two test codes to your computer, and run them both in both environments.  (One should only work in `numpy1-test`, and the other should only work in `numpy2-test`)  

3. Experiment with creating your own virtual environment(s) and then running your own code.  For example, you may want to install `python`, `numpy`, `pandas`, `jupyter`, `matplotlib`. 

*Hint* : In order to switch environments in the Anaconda Navigator, you need to enter the environments tab to activate a given environment.  Once an environment is activated, you can then go back to the main screen of the Navigator and open Jupyter.  If you are working from the terminal (i.e., you installed miniforge), you will want to use the `activate` and `deactivate` commands.  If you are working inside VS Code, you can also switch your environment via the `Select Kernel` button in the upper right of your window when viewing either .ipynb file (this button may way the active environment's name instead of "Select Kernel").
