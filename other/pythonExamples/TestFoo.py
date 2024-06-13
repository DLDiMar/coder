# example_program.py
import foo_param

# Import the required components from foo_param
from foo_param.core import core_main
from foo_param.gui.shape_app import ShapeApp
from foo_param.models.sphere_model import SphereModel
from foo_param.models.input_model import InputModel
from foo_param.utils.csv_logger import log_result

# Use the components as needed
def main():
    # Example usage of core_main function
    core_main()
    
    # Example usage of SphereModel
    radius = 5
    sphere = SphereModel(radius)
    volume = sphere.calculate()
    print(f"Volume of the sphere with radius {radius}: {volume}")

    # Example usage of InputModel
    input_model = InputModel()
    input_model.sphere_input("5", "2")
    print(f"Input model parameters: {input_model.param1_value}, precision: {input_model.precision}")

    # Example usage of logging function
    log_result("sphere", input_model.param1_name, input_model.param1_value, volume_output=volume)
    
    # GUI usage would typically involve running the main loop, not directly usable in a script like this
    # But here's how you could instantiate it (though not running the main loop here)
    # root = tk.Tk()
    # app = ShapeApp(root)

if __name__ == "__main__":
    main()
