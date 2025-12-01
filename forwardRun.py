from isaaclab.app import AppLauncher
from isaaclab.sim import SimulationContext
import isaaclab.sim as sim_utils
from isaaclab.assets import Articulation, ArticulationCfg
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR
import numpy as np

# Launch the Isaac Lab app
app_launcher = AppLauncher()
simulation_app = app_launcher.app

# -------------------------------------------------------------
# CONFIG: Choose your robot USD
# -------------------------------------------------------------
ROBOT_USD = f"{ISAAC_NUCLEUS_DIR}/Robots/Jetbot/jetbot.usd"   # example
# You can replace it with ANY robot USD path

robot_cfg = ArticulationCfg(
    prim_path="/World/Robot",
    spawn=sim_utils.UsdFileCfg(
        usd_path=ROBOT_USD
    )
)

# -------------------------------------------------------------
# Create simulation
# -------------------------------------------------------------
sim_cfg = sim_utils.SimulationCfg()
sim = SimulationContext(sim_cfg)

# Add ground plane
ground = sim_utils.GroundPlaneCfg()
sim.add_ground_plane(ground)

# Spawn robot
robot = Articulation(robot_cfg)

# Play the scene
sim.play()

# -------------------------------------------------------------
# Simple control loop: move forward
# -------------------------------------------------------------
desired_linear_speed = 1.0  # m/s forward

print("Moving robot forward...")

while simulation_app.is_running():
    # Step the physics
    sim.step()
    
    # Apply forward base velocity
    robot.set_linear_velocity(np.array([desired_linear_speed, 0.0, 0.0]))
