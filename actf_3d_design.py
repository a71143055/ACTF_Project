"""
ACTF (Android Cyborg Transformers) 3D Design
Based on README.md specifications
- Outer skeleton: Graphene polymer liquid crystal with carbon nanotube reinforcement
- Inner skeleton: Stem cell cultivation structure for artificial organs
- Modular assembly design inspired by Transformers
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyBboxPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation

class ACTF3DDesigner:
    def __init__(self):
        self.fig = plt.figure(figsize=(16, 12))
        self.fig.patch.set_facecolor('#1a1a2e')
        
    def create_humanoid_base(self):
        """Create basic humanoid structure"""
        # Body proportions (normalized)
        self.head_center = np.array([0, 0, 1.8])
        self.torso_center = np.array([0, 0, 1.2])
        self.arm_length = 0.7
        self.leg_length = 0.9
        
    def draw_sphere(self, center, radius, color, alpha=0.7, label='', ax=None):
        """Draw a 3D sphere"""
        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
        y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
        z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
        
        if ax is None:
            ax = self.fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, color=color, alpha=alpha, label=label)
        
    def draw_cylinder(self, start, end, radius, color, alpha=0.7, ax=None):
        """Draw a 3D cylinder"""
        if ax is None:
            ax = self.fig.add_subplot(111, projection='3d')
        
        # Vector along cylinder axis
        v = end - start
        length = np.linalg.norm(v)
        v = v / length
        
        # Create perpendicular vectors
        if abs(v[2]) < 0.9:
            perp1 = np.cross(v, np.array([0, 0, 1]))
        else:
            perp1 = np.cross(v, np.array([0, 1, 0]))
        perp1 = perp1 / np.linalg.norm(perp1)
        perp2 = np.cross(v, perp1)
        
        # Create cylinder surface
        theta = np.linspace(0, 2*np.pi, 20)
        z_cyl = np.linspace(0, length, 10)
        theta_grid, z_grid = np.meshgrid(theta, z_cyl)
        
        x_grid = start[0] + radius * (np.cos(theta_grid) * perp1[0] + np.sin(theta_grid) * perp2[0]) + z_grid * v[0]
        y_grid = start[1] + radius * (np.cos(theta_grid) * perp1[1] + np.sin(theta_grid) * perp2[1]) + z_grid * v[1]
        z_grid = start[2] + radius * (np.cos(theta_grid) * perp1[2] + np.sin(theta_grid) * perp2[2]) + z_grid * v[2]
        
        ax.plot_surface(x_grid, y_grid, z_grid, color=color, alpha=alpha)
        
    def draw_armor_plate(self, vertices, color, alpha=0.6, ax=None):
        """Draw an armor plate (polygon)"""
        if ax is None:
            ax = self.fig.add_subplot(111, projection='3d')
        poly = Poly3DCollection([vertices], alpha=alpha)
        poly.set_facecolor(color)
        poly.set_edgecolor('black')
        poly.set_linewidth(0.5)
        ax.add_collection3d(poly)
        
    def create_inner_skeleton(self, ax=None):
        """Create inner skeleton structure for stem cell cultivation"""
        if ax is None:
            ax = self.fig.add_subplot(111, projection='3d')
        
        # Spinal column (vertebrae structure)
        for i in range(10):
            z_pos = 0.5 + i * 0.1
            self.draw_sphere(np.array([0, 0, z_pos]), 0.08, '#4a90d9', 0.5, ax=ax)
        
        # Rib cage (protection for organs)
        for i in range(6):
            angle = i * np.pi / 3
            x = 0.25 * np.cos(angle)
            y = 0.25 * np.sin(angle)
            self.draw_cylinder(np.array([x, y, 1.0]), np.array([x, y, 1.4]), 0.02, '#4a90d9', 0.6, ax=ax)
        
        # Pelvic structure
        self.draw_sphere(np.array([0, 0, 0.5]), 0.15, '#4a90d9', 0.5, ax=ax)
        
        # Arm bones (humerus, radius, ulna)
        self.draw_cylinder(np.array([0.3, 0, 1.3]), np.array([0.5, 0, 0.9]), 0.04, '#4a90d9', 0.5, ax=ax)
        self.draw_cylinder(np.array([0.5, 0, 0.9]), np.array([0.6, 0, 0.5]), 0.03, '#4a90d9', 0.5, ax=ax)
        
        # Leg bones (femur, tibia)
        self.draw_cylinder(np.array([0.15, 0, 1.0]), np.array([0.15, 0, 0.5]), 0.05, '#4a90d9', 0.5, ax=ax)
        self.draw_cylinder(np.array([0.15, 0, 0.5]), np.array([0.15, 0, 0.0]), 0.04, '#4a90d9', 0.5, ax=ax)
        
        # Organ chambers (stem cell cultivation areas)
        # Heart chamber
        self.draw_sphere(np.array([0.1, 0, 1.25]), 0.08, '#ff6b6b', 0.7, ax=ax)
        # Lung chambers
        self.draw_sphere(np.array([0.05, 0.15, 1.3]), 0.07, '#6bcf7f', 0.7, ax=ax)
        self.draw_sphere(np.array([0.05, -0.15, 1.3]), 0.07, '#6bcf7f', 0.7, ax=ax)
        # Brain chamber
        self.draw_sphere(np.array([0, 0, 1.75]), 0.12, '#ffd93d', 0.7, ax=ax)
        
    def create_outer_skeleton(self, ax=None):
        """Create outer skeleton armor with graphene polymer liquid crystal"""
        # Chest armor plate
        chest_vertices = np.array([
            [0.35, 0.2, 1.5], [0.35, -0.2, 1.5],
            [0.35, -0.2, 1.0], [0.35, 0.2, 1.0]
        ])
        self.draw_armor_plate(chest_vertices, '#2d3436', 0.4, ax=ax)
        
        # Back armor plate
        back_vertices = np.array([
            [-0.35, 0.2, 1.5], [-0.35, -0.2, 1.5],
            [-0.35, -0.2, 1.0], [-0.35, 0.2, 1.0]
        ])
        self.draw_armor_plate(back_vertices, '#2d3436', 0.4, ax=ax)
        
        # Shoulder armor (left and right)
        for side in [1, -1]:
            shoulder_center = np.array([side * 0.4, 0, 1.45])
            self.draw_sphere(shoulder_center, 0.12, '#636e72', 0.6, ax=ax)
            
            # Shoulder pauldrons
            pauldron_vertices = np.array([
                [side * 0.5, 0.15, 1.55], [side * 0.5, -0.15, 1.55],
                [side * 0.35, -0.15, 1.35], [side * 0.35, 0.15, 1.35]
            ])
            self.draw_armor_plate(pauldron_vertices, '#2d3436', 0.5, ax=ax)
        
        # Helmet
        helmet_vertices = np.array([
            [0.2, 0.15, 1.95], [0.2, -0.15, 1.95],
            [0.2, -0.15, 1.65], [0.2, 0.15, 1.65]
        ])
        self.draw_armor_plate(helmet_vertices, '#2d3436', 0.5, ax=ax)
        
        # Visor
        visor_vertices = np.array([
            [0.22, 0.1, 1.85], [0.22, -0.1, 1.85],
            [0.22, -0.1, 1.75], [0.22, 0.1, 1.75]
        ])
        self.draw_armor_plate(visor_vertices, '#00cec9', 0.8, ax=ax)
        
        # Arm armor (forearm guards)
        for side in [1, -1]:
            arm_guard_vertices = np.array([
                [side * 0.65, 0.1, 0.7], [side * 0.65, -0.1, 0.7],
                [side * 0.55, -0.1, 0.5], [side * 0.55, 0.1, 0.5]
            ])
            self.draw_armor_plate(arm_guard_vertices, '#2d3436', 0.5, ax=ax)
        
        # Leg armor (thigh guards)
        for side in [1, -1]:
            thigh_guard_vertices = np.array([
                [side * 0.25, 0.12, 0.9], [side * 0.25, -0.12, 0.9],
                [side * 0.2, -0.12, 0.6], [side * 0.2, 0.12, 0.6]
            ])
            self.draw_armor_plate(thigh_guard_vertices, '#2d3436', 0.5, ax=ax)
            
        # Shin guards
        for side in [1, -1]:
            shin_guard_vertices = np.array([
                [side * 0.22, 0.1, 0.45], [side * 0.22, -0.1, 0.45],
                [side * 0.18, -0.1, 0.1], [side * 0.18, 0.1, 0.1]
            ])
            self.draw_armor_plate(shin_guard_vertices, '#2d3436', 0.5, ax=ax)
        
    def create_carbon_nanotube_layer(self, ax=None):
        """Add carbon nanotube reinforcement layer (harder than liquid crystal)"""
        if ax is None:
            ax = self.fig.add_subplot(111, projection='3d')
        
        # Carbon nanotube mesh pattern on chest
        for i in range(5):
            for j in range(3):
                x = 0.36 + i * 0.02
                y = -0.15 + j * 0.15
                z = 1.05 + i * 0.1
                self.draw_sphere(np.array([x, y, z]), 0.01, '#00b894', 0.9, ax=ax)
        
        # Nanotube reinforcement on joints
        joint_positions = [
            [0.4, 0, 1.45],  # Shoulders
            [-0.4, 0, 1.45],
            [0.6, 0, 0.7],   # Elbows
            [-0.6, 0, 0.7],
            [0.2, 0, 0.5],   # Knees
            [-0.2, 0, 0.5]
        ]
        
        for pos in joint_positions:
            for angle in range(0, 360, 45):
                rad = np.radians(angle)
                offset = np.array([0.03 * np.cos(rad), 0.03 * np.sin(rad), 0])
                self.draw_sphere(np.array(pos) + offset, 0.008, '#00b894', 0.8, ax=ax)
        
    def create_graphene_polymer_effect(self, ax=None):
        """Visualize graphene polymer liquid crystal (intermediate solid-liquid state)"""
        if ax is None:
            ax = self.fig.add_subplot(111, projection='3d')
        
        # Create flowing liquid crystal effect
        for i in range(20):
            x = 0.3 + 0.1 * np.sin(i * 0.5)
            y = 0.2 * np.cos(i * 0.3)
            z = 1.0 + i * 0.03
            alpha = 0.3 + 0.2 * np.sin(i * 0.2)
            self.draw_sphere(np.array([x, y, z]), 0.02, '#74b9ff', alpha, ax=ax)
            self.draw_sphere(np.array([-x, y, z]), 0.02, '#74b9ff', alpha, ax=ax)
            
    def visualize_complete_design(self):
        """Create complete ACTF 3D visualization"""
        self.create_humanoid_base()
        
        # Create subplot for different views
        ax1 = self.fig.add_subplot(2, 2, 1, projection='3d')
        ax2 = self.fig.add_subplot(2, 2, 2, projection='3d')
        ax3 = self.fig.add_subplot(2, 2, 3, projection='3d')
        ax4 = self.fig.add_subplot(2, 2, 4, projection='3d')
        
        # View 1: Inner Skeleton
        ax1.set_title('Inner Skeleton (Stem Cell Cultivation)', color='white', fontsize=10)
        self.create_inner_skeleton(ax=ax1)
        ax1.set_xlim([-0.5, 0.5])
        ax1.set_ylim([-0.5, 0.5])
        ax1.set_zlim([0, 2])
        ax1.set_xlabel('X', color='white')
        ax1.set_ylabel('Y', color='white')
        ax1.set_zlabel('Z', color='white')
        ax1.tick_params(colors='white')
        
        # View 2: Outer Skeleton
        ax2.set_title('Outer Skeleton (Graphene Polymer Armor)', color='white', fontsize=10)
        self.create_outer_skeleton(ax=ax2)
        ax2.set_xlim([-0.7, 0.7])
        ax2.set_ylim([-0.5, 0.5])
        ax2.set_zlim([0, 2])
        ax2.set_xlabel('X', color='white')
        ax2.set_ylabel('Y', color='white')
        ax2.set_zlabel('Z', color='white')
        ax2.tick_params(colors='white')
        
        # View 3: Carbon Nanotube Reinforcement
        ax3.set_title('Carbon Nanotube Reinforcement', color='white', fontsize=10)
        self.create_outer_skeleton(ax=ax3)
        self.create_carbon_nanotube_layer(ax=ax3)
        ax3.set_xlim([-0.7, 0.7])
        ax3.set_ylim([-0.5, 0.5])
        ax3.set_zlim([0, 2])
        ax3.set_xlabel('X', color='white')
        ax3.set_ylabel('Y', color='white')
        ax3.set_zlabel('Z', color='white')
        ax3.tick_params(colors='white')
        
        # View 4: Complete Assembly
        ax4.set_title('Complete ACTF Assembly', color='white', fontsize=10)
        self.create_inner_skeleton(ax=ax4)
        self.create_outer_skeleton(ax=ax4)
        self.create_carbon_nanotube_layer(ax=ax4)
        self.create_graphene_polymer_effect(ax=ax4)
        ax4.set_xlim([-0.7, 0.7])
        ax4.set_ylim([-0.5, 0.5])
        ax4.set_zlim([0, 2])
        ax4.set_xlabel('X', color='white')
        ax4.set_ylabel('Y', color='white')
        ax4.set_zlabel('Z', color='white')
        ax4.tick_params(colors='white')
        ax4.view_init(elev=20, azim=45)
        
        plt.tight_layout()
        plt.savefig('actf_3d_design.png', dpi=300, bbox_inches='tight', facecolor='#1a1a2e')
        plt.show()
        
    def create_single_view_design(self):
        """Create single comprehensive view"""
        ax = self.fig.add_subplot(111, projection='3d')
        self.create_humanoid_base()
        
        # Build complete structure
        self.create_inner_skeleton(ax=ax)
        self.create_outer_skeleton(ax=ax)
        self.create_carbon_nanotube_layer(ax=ax)
        self.create_graphene_polymer_effect(ax=ax)
        
        # Set labels and title
        ax.set_title('ACTF (Android Cyborg Transformers) - Complete 3D Design', 
                     color='white', fontsize=14, pad=20)
        ax.set_xlabel('X (meters)', color='white')
        ax.set_ylabel('Y (meters)', color='white')
        ax.set_zlabel('Z (meters)', color='white')
        
        # Set limits
        ax.set_xlim([-0.8, 0.8])
        ax.set_ylim([-0.6, 0.6])
        ax.set_zlim([0, 2.2])
        
        # Style
        ax.tick_params(colors='white')
        ax.grid(True, alpha=0.3)
        ax.set_facecolor('#16213e')
        
        # Set viewing angle
        ax.view_init(elev=25, azim=45)
        
        # Add legend
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Inner Skeleton (Stem Cells)',
                   markerfacecolor='#4a90d9', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Outer Armor (Graphene)',
                   markerfacecolor='#2d3436', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Carbon Nanotubes',
                   markerfacecolor='#00b894', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Liquid Crystal',
                   markerfacecolor='#74b9ff', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Organ Chambers',
                   markerfacecolor='#ff6b6b', markersize=10)
        ]
        ax.legend(handles=legend_elements, loc='upper left', 
                 facecolor='#1a1a2e', edgecolor='white', labelcolor='white')
        
        plt.tight_layout()
        plt.savefig('actf_complete_design.png', dpi=300, bbox_inches='tight', facecolor='#1a1a2e')
        plt.show()

def main():
    """Main function to run ACTF 3D design"""
    print("ACTF 3D Design Generator")
    print("=" * 50)
    print("Creating Android Cyborg Transformers 3D visualization...")
    print("Based on README.md specifications:")
    print("- Inner Skeleton: Stem cell cultivation structure")
    print("- Outer Skeleton: Graphene polymer liquid crystal armor")
    print("- Carbon Nanotube: Hard reinforcement layer")
    print("- Modular assembly design")
    print("=" * 50)
    
    designer = ACTF3DDesigner()
    
    # Choose visualization mode
    print("\nGenerating comprehensive multi-view design...")
    designer.visualize_complete_design()
    
    print("\nGenerating single complete view...")
    designer = ACTF3DDesigner()
    designer.create_single_view_design()
    
    print("\n3D design complete! Images saved as:")
    print("- actf_3d_design.png (multi-view)")
    print("- actf_complete_design.png (single view)")
    print("\nOpen these files in VS Code to view the 3D design.")

if __name__ == "__main__":
    main()
