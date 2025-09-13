import tkinter as tk
from tkinter import simpledialog, messagebox
import igraph as ig
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_graph():
    plt.clf()
    visual_style = {"vertex_color": [color_map.get(node.index, 'gray') for node in G.vs]}
    ig.plot(G, layout=layout, target=ax, **visual_style)
    canvas.draw()

def add_node():
    node = simpledialog.askstring("Input", "Enter node name:")
    if node and node not in node_labels:
        G.add_vertex(name=node)
        node_labels.append(node)
        draw_graph()

def add_edge():
    node1 = simpledialog.askstring("Input", "Enter first node:")
    node2 = simpledialog.askstring("Input", "Enter second node:")
    if node1 in node_labels and node2 in node_labels:
        G.add_edge(node_labels.index(node1), node_labels.index(node2))
        draw_graph()
    else:
        messagebox.showerror("Error", "Both nodes must exist.")

def color_graph():
    global color_map
    color_map = {}  # Reset color map
    try:
        coloring = G.coloring_greedy()
        colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        for node, color_id in enumerate(coloring):
            color_map[node] = colors[color_id % len(colors)]
        draw_graph()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Graph Coloring GUI")
G = ig.Graph()
node_labels = []
color_map = {}
layout = G.layout("kk")

frame = tk.Frame(root)
frame.pack(side=tk.LEFT, padx=10, pady=10)

canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.RIGHT)

fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.get_tk_widget().pack()

tk.Button(frame, text="Add Node", command=add_node).pack(pady=5)
tk.Button(frame, text="Add Edge", command=add_edge).pack(pady=5)
tk.Button(frame, text="Color Graph", command=color_graph).pack(pady=5)

draw_graph()
root.mainloop()
