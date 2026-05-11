import numpy as np
import matplotlib.pyplot as plt

def simulate_1d_random_walk(d, v, num_simulations=1000, max_steps=100000):
    """Simulate 1D random walk with alternating forward/backward steps"""
    times = []
    
    for _ in range(num_simulations):
        position = 0
        time = 0
        steps = 0
        
        while position < d and steps < max_steps:
            # Forward step: random distance between 1 and 10
            forward = np.random.uniform(1, 10)
            position += forward
            time += forward / v
            
            if position >= d:
                break
            
            # Backward step: random distance between 1 and 5
            backward = np.random.uniform(1, 5)
            position -= backward
            time += backward / v
            
            steps += 1
        
        if steps < max_steps:
            times.append(time)
    
    return np.array(times)

def simulate_2d_random_walk(d, v, num_simulations=1000, max_steps=100000):
    """Simulate 2D random walk with alternating forward/backward steps"""
    times = []
    
    for _ in range(num_simulations):
        x, y = 0, 0
        time = 0
        steps = 0
        
        while np.sqrt(x**2 + y**2) < d and steps < max_steps:
            # Forward step: random distance and direction
            forward_dist = np.random.uniform(1, 10)
            forward_angle = np.random.uniform(0, 2 * np.pi)
            x += forward_dist * np.cos(forward_angle)
            y += forward_dist * np.sin(forward_angle)
            time += forward_dist / v
            
            if np.sqrt(x**2 + y**2) >= d:
                break
            
            # Backward step: random distance and direction
            backward_dist = np.random.uniform(1, 5)
            backward_angle = np.random.uniform(0, 2 * np.pi)
            x += backward_dist * np.cos(backward_angle)
            y += backward_dist * np.sin(backward_angle)
            time += backward_dist / v
            
            steps += 1
        
        if steps < max_steps:
            times.append(time)
    
    return np.array(times)

def calculate_cdf(times):
    """Calculate cumulative distribution function"""
    sorted_times = np.sort(times)
    cdf = np.arange(1, len(sorted_times) + 1) / len(sorted_times)
    return sorted_times, cdf

def plot_cdfs(times_1d, times_2d):
    """Plot CDFs for both 1D and 2D cases"""
    # Calculate CDFs
    times_1d_sorted, cdf_1d = calculate_cdf(times_1d)
    times_2d_sorted, cdf_2d = calculate_cdf(times_2d)
    
    # Create plot
    plt.figure(figsize=(12, 6))
    
    plt.plot(times_1d_sorted, cdf_1d, label='1D Random Walk', linewidth=2)
    plt.plot(times_2d_sorted, cdf_2d, label='2D Random Walk', linewidth=2)
    
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Cumulative Probability', fontsize=12)
    plt.title('CDF: Time to Reach Distance d', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return plt

# Parameters
d = 100  # distance
v = 1    # velocity
num_simulations = 1000

# Run simulations
print("Running 1D simulation...")
times_1d = simulate_1d_random_walk(d, v, num_simulations)

print("Running 2D simulation...")
times_2d = simulate_2d_random_walk(d, v, num_simulations)

# Print statistics
print("\n=== Statistics ===")
print(f"\n1D Random Walk:")
print(f"  Mean time: {np.mean(times_1d):.2f}")
print(f"  Median time: {np.median(times_1d):.2f}")
print(f"  Std dev: {np.std(times_1d):.2f}")
print(f"  Success rate: {len(times_1d)/num_simulations*100:.1f}%")

print(f"\n2D Random Walk:")
print(f"  Mean time: {np.mean(times_2d):.2f}")
print(f"  Median time: {np.median(times_2d):.2f}")
print(f"  Std dev: {np.std(times_2d):.2f}")
print(f"  Success rate: {len(times_2d)/num_simulations*100:.1f}%")

# Plot CDFs
plt = plot_cdfs(times_1d, times_2d)
plt.show()