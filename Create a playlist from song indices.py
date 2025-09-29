import numpy as np

# Array of 20 songs
songs = np.array(['Song A', 'Song B', 'Song C', 'Song D', 'Song E',
                  'Song F', 'Song G', 'Song H', 'Song I', 'Song J',
                  'Song K', 'Song L', 'Song M', 'Song N', 'Song O',
                  'Song P', 'Song Q', 'Song R', 'Song S', 'Song T'])

# Get indices form user
indices = input().split()
indices = [int(score) for score in indices]

# Create a playlist by selecting songs using their indices
# Hint: Use integer array indexing

playlist = songs[indices]

# Print the playlist
print(playlist)
