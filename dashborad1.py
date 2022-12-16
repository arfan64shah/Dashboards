from flask import Flask, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def dashboard():
  # Generate some data to plot
  x = [1, 2, 3, 4, 5]
  y = [1, 4, 9, 16, 25]
  
  # Create a Matplotlib figure and axis
  fig, ax = plt.subplots()
  
  # Plot the data and set the x and y labels
  ax.plot(x, y)
  ax.set_xlabel('X Values')
  ax.set_ylabel('Y Values')
  
  # Save the figure to a temporary file
  fig.savefig('static/plot.png')
  
  # Render the template with the plot image
  return render_template('dashboard.html', plot_url='static/plot.png')

if __name__ == '__main__':
  app.run()