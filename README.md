# Orakel

> brainstorm with llama/anything

### Configuration

By default the app runs in production mode. Configure the app with `.env`
file in the same directory level as `app.py`. The file should [stricly] follow the schema of:

```text
KEY=VALUE
```

example:

```text
PORT=5005
DEBUG=1
HOST=0.0.0.0
MODEL=None
```

if your computer is not powerful enough for a local lanaugage model just do 

MODEL=None 

if you put nothing it will be 

MODEL=llama3.1




> at this commit the env parsing doesn't allow variables inside the values

### Running

run in development with `python3 app.py`

> [!danger] this server is only for development.

### Stack

- frontend: vanillajs, Yes! we raw-dogged it :P
- backend: flask and ollama library





### Features

#### ✅ Working
- **Node Interaction**
  - 🖱️ **Grab and move** individual nodes
  - 🔄 **Real-time line updates** when nodes are moved
  - ❌ **Delete individual nodes**

- **Context Menu**
  - ✨ **Double-click** to add nodes to the context menu
  - 🗑️ **UI support** for removing nodes from the context menu

- **Multi-Selection**
  - ⇧ **Multi-select nodes** with Shift
  - 🧹 **Delete multiple nodes** at once

#### 🚧 In Progress
- **Multi-Node Grab**


Built in B4Y3RW4LD Hackathon.





We might use json like:

{
  "graph": {
    "nodes": {
      "nodeID1" : {

        "x": 1,
        "y": 1,
        "text": "Alice"
      },
      "nodeID2":{
       "x": 1,
        "y": 1,
        "text": "Bob"
      }
    },
    "edges": [["nodeID1","nodeID2","parent"]]
  }
}
