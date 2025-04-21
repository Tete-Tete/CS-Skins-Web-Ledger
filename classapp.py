import streamlit as st
import heapq

# Dijkstra 算法实现
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]

    return path, distances[end] if distances[end] != float('inf') else None

# Streamlit 页面
st.set_page_config(page_title="Shortest Path Finder", layout="centered")
st.title("🚗 Shortest Path Finder using Dijkstra's Algorithm")

# 输入节点（城市）
town_input = st.text_input("Enter all towns (separated by spaces):", "Origin A B C D E Destination")
towns = town_input.strip().split()

# 初始化图
graph = {town: {} for town in towns}

st.markdown("### Enter Connections (each line: Town1,Town2,Distance)")
edge_input = st.text_area("Example:\nOrigin,A,40\nA,B,10\nB,Destination,30", height=200)

if edge_input:
    for line in edge_input.strip().split("\n"):
        try:
            t1, t2, dist = line.strip().split(",")
            dist = float(dist)
            graph[t1][t2] = dist
            graph[t2][t1] = dist  # 双向边
        except:
            st.error(f"Invalid line format: {line}")

# 选择起点和终点
col1, col2 = st.columns(2)
with col1:
    start = st.selectbox("Start town", towns)
with col2:
    end = st.selectbox("End town", towns, index=len(towns)-1)

# 点击按钮计算路径
if st.button("Find Shortest Path"):
    if start == end:
        st.warning("Start and end towns must be different.")
    else:
        path, distance = dijkstra(graph, start, end)
        if distance is not None:
            st.success(f"Shortest path: {' -> '.join(path)}")
            st.info(f"Total distance: {distance} units")
        else:
            st.error("No path found between the selected towns.")