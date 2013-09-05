# Loading heterogenous data from a text file into a Numpy array

# Define the dtype descriptor
dt = dict(names = ('station', 'lat', 'lon', 'elev'),
          formats = ('S4', np.float32, np.float32, np.float32) )

# Load the file
stations = np.loadtxt('stations.txt', dtype=dt)

# Print a few basic statistics
print 'Mean latitude:', stations['lat'].mean()
print 'Mean longitude:', stations['lon'].mean()
print 'Max elevation:', stations['elev'].max(), 'km'

# Use argmax to find the index of the maximum elevation, and read the station name
print 'Station at max elevation', stations['station'][np.argmax(stations['elev'])]