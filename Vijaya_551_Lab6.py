
import random
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# =========================================================
# MEDIQUEUE: FIVE TREE DATA STRUCTURES
# =========================================================

st.set_page_config(page_title="MediQueue", page_icon="🏥", layout="wide")
st.title("🏥 MediQueue")
st.subheader("Patient Management with Five Tree Data Structures")
st.write("Insert, search, delete, visualize, and animate patient records.")

# =========================================================
# 1. PLAIN BINARY SEARCH TREE
# =========================================================

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            return
        node = self.root
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = BSTNode(key)
                    return
                node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = BSTNode(key)
                    return
                node = node.right
            else:
                return

    def search(self, key):
        node = self.root
        while node:
            if node.key == key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = node.right
            while successor.left:
                successor = successor.left
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node


# =========================================================
# 2. AVL TREE
# =========================================================

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def update(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        temp = x.right
        x.right = y
        y.left = temp
        self.update(y)
        self.update(x)
        return x

    def rotate_left(self, x):
        y = x.right
        temp = y.left
        y.left = x
        x.right = temp
        self.update(x)
        self.update(y)
        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        self.update(node)
        b = self.balance(node)

        if b > 1 and key < node.left.key:
            return self.rotate_right(node)
        if b < -1 and key > node.right.key:
            return self.rotate_left(node)
        if b > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if b < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def search(self, key):
        node = self.root
        while node:
            if node.key == key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = node.right
            while successor.left:
                successor = successor.left
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        self.update(node)
        b = self.balance(node)

        if b > 1 and self.balance(node.left) >= 0:
            return self.rotate_right(node)
        if b > 1 and self.balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if b < -1 and self.balance(node.right) <= 0:
            return self.rotate_left(node)
        if b < -1 and self.balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node


# =========================================================
# 3. RED-BLACK TREE
# =========================================================

RED = "RED"
BLACK = "BLACK"


class RBNode:
    def __init__(self, key=None, color=BLACK):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode()
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        self.root = self.NIL

    def search(self, key):
        node = self.root
        while node != self.NIL:
            if node.key == key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent

        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent

        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def insert(self, key):
        z = RBNode(key, RED)
        z.left = self.NIL
        z.right = self.NIL
        parent = self.NIL
        node = self.root

        while node != self.NIL:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return

        z.parent = parent
        if parent == self.NIL:
            self.root = z
        elif key < parent.key:
            parent.left = z
        else:
            parent.right = z

        self.insert_fix(z)

    def insert_fix(self, z):
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                uncle = z.parent.parent.right

                if uncle.color == RED:
                    z.parent.color = BLACK
                    uncle.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else:
                uncle = z.parent.parent.left

                if uncle.color == RED:
                    z.parent.color = BLACK
                    uncle.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)

        self.root.color = BLACK

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def transplant(self, old, new):
        if old.parent == self.NIL:
            self.root = new
        elif old == old.parent.left:
            old.parent.left = new
        else:
            old.parent.right = new
        new.parent = old.parent

    def delete(self, key):
        z = self.root
        while z != self.NIL and z.key != key:
            z = z.left if key < z.key else z.right

        if z == self.NIL:
            return

        y = z
        original_color = y.color

        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            original_color = y.color
            x = y.right

            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if original_color == BLACK:
            self.delete_fix(x)

        if self.root != self.NIL:
            self.root.parent = self.NIL
        self.NIL.parent = self.NIL

    def delete_fix(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right

                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == BLACK and w.right.color == BLACK:
                    if w != self.NIL:
                        w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left

                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    if w != self.NIL:
                        w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = BLACK


# =========================================================
# 4. B-TREE (MINIMUM DEGREE 2)
# =========================================================

class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTree:
    def __init__(self, degree=2):
        self.t = degree
        self.root = BTreeNode()

    def search(self, key):
        def find(node):
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if i < len(node.keys) and node.keys[i] == key:
                return True
            if node.leaf:
                return False
            return find(node.children[i])
        return find(self.root)

    def insert(self, key):
        if self.search(key):
            return

        if len(self.root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root

        self.insert_nonfull(self.root, key)

    def split_child(self, parent, index):
        t = self.t
        old = parent.children[index]
        new = BTreeNode(old.leaf)
        median = old.keys[t - 1]

        new.keys = old.keys[t:]
        old.keys = old.keys[:t - 1]

        if not old.leaf:
            new.children = old.children[t:]
            old.children = old.children[:t]

        parent.keys.insert(index, median)
        parent.children.insert(index + 1, new)

    def insert_nonfull(self, node, key):
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
            return

        i = len(node.keys) - 1
        while i >= 0 and key < node.keys[i]:
            i -= 1
        i += 1

        if len(node.children[i].keys) == 2 * self.t - 1:
            self.split_child(node, i)
            if key > node.keys[i]:
                i += 1

        self.insert_nonfull(node.children[i], key)

    def delete(self, key):
        self._delete(self.root, key)

        if not self.root.leaf and len(self.root.keys) == 0:
            self.root = self.root.children[0]

    def merge(self, parent, i):
        left = parent.children[i]
        right = parent.children[i + 1]

        left.keys.append(parent.keys.pop(i))
        left.keys.extend(right.keys)

        if not left.leaf:
            left.children.extend(right.children)

        parent.children.pop(i + 1)

    def _delete(self, node, key):
        t = self.t
        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == key:
            if node.leaf:
                node.keys.pop(i)
                return

            left = node.children[i]
            right = node.children[i + 1]

            if len(left.keys) >= t:
                pred = left
                while not pred.leaf:
                    pred = pred.children[-1]
                replacement = pred.keys[-1]
                node.keys[i] = replacement
                self._delete(left, replacement)

            elif len(right.keys) >= t:
                succ = right
                while not succ.leaf:
                    succ = succ.children[0]
                replacement = succ.keys[0]
                node.keys[i] = replacement
                self._delete(right, replacement)

            else:
                self.merge(node, i)
                self._delete(left, key)
            return

        if node.leaf:
            return

        # Ensure the child has enough keys before descending.
        if len(node.children[i].keys) == t - 1:
            if i > 0 and len(node.children[i - 1].keys) >= t:
                child = node.children[i]
                sibling = node.children[i - 1]

                child.keys.insert(0, node.keys[i - 1])
                node.keys[i - 1] = sibling.keys.pop()

                if not sibling.leaf:
                    child.children.insert(0, sibling.children.pop())

            elif i < len(node.keys) and len(node.children[i + 1].keys) >= t:
                child = node.children[i]
                sibling = node.children[i + 1]

                child.keys.append(node.keys[i])
                node.keys[i] = sibling.keys.pop(0)

                if not sibling.leaf:
                    child.children.append(sibling.children.pop(0))

            else:
                if i < len(node.keys):
                    self.merge(node, i)
                else:
                    self.merge(node, i - 1)
                    i -= 1

        self._delete(node.children[i], key)


# =========================================================
# 5. TREAP
# =========================================================

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 999)
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreapNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
            if node.left.priority < node.priority:
                node = self.rotate_right(node)

        elif key > node.key:
            node.right = self._insert(node.right, key)
            if node.right.priority < node.priority:
                node = self.rotate_left(node)

        return node

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            if node.left.priority < node.right.priority:
                node = self.rotate_right(node)
                node.right = self._delete(node.right, key)
            else:
                node = self.rotate_left(node)
                node.left = self._delete(node.left, key)

        return node


# =========================================================
# 6. TREE CREATION AND HEIGHT
# =========================================================

def create_trees():
    return BST(), AVL(), RedBlackTree(), BTree(), Treap()


def binary_height(node, nil=None):
    if node is None or (nil is not None and node == nil):
        return 0
    return 1 + max(
        binary_height(node.left, nil),
        binary_height(node.right, nil)
    )


def btree_height(node):
    if node is None:
        return 0
    if node.leaf:
        return 1
    return 1 + btree_height(node.children[0])


# =========================================================
# 7. TREE DRAWING FUNCTIONS
# =========================================================

def draw_binary_tree(root, title, patients, nil=None, treap=False):
    if root is None or (nil is not None and root == nil):
        st.info("This tree is empty.")
        return

    graph = nx.Graph()
    positions = {}
    labels = {}
    colors = {}
    counter = [0]

    def visit(node, depth):
        if node is None or (nil is not None and node == nil):
            return

        visit(node.left, depth + 1)

        x = counter[0]
        counter[0] += 1

        graph.add_node(node.key)
        positions[node.key] = (x, -depth)

        name = patients.get(node.key, "")
        labels[node.key] = f"{node.key}\n{name}"

        if hasattr(node, "color"):
            colors[node.key] = (
                "#D62828" if node.color == RED else "#222222"
            )
        else:
            colors[node.key] = "#9BD1E5"

        if treap:
            labels[node.key] += f"\nP:{node.priority}"

        for child in (node.left, node.right):
            if child is not None and (nil is None or child != nil):
                graph.add_edge(node.key, child.key)

        visit(node.right, depth + 1)

    visit(root, 0)

    fig, ax = plt.subplots(figsize=(max(8, len(graph.nodes()) * 1.2), 5))

    nx.draw_networkx(
        graph,
        pos=positions,
        labels=labels,
        ax=ax,
        node_color=[colors[n] for n in graph.nodes()],
        edgecolors="black",
        node_size=1800,
        font_size=8,
        arrows=False
    )

    if title.startswith("Red-Black"):
        for item in ax.texts:
            item.set_color("white")

    ax.set_title(title)
    ax.axis("off")
    st.pyplot(fig)
    plt.close(fig)


def draw_btree(root, title):
    graph = nx.Graph()
    positions = {}
    labels = {}
    counter = [0]

    def visit(node, depth, parent_id=None):
        node_id = id(node)
        graph.add_node(node_id)

        x = counter[0]
        counter[0] += 1

        positions[node_id] = (x, -depth)
        labels[node_id] = " | ".join(map(str, node.keys))

        if parent_id is not None:
            graph.add_edge(parent_id, node_id)

        if not node.leaf:
            for child in node.children:
                visit(child, depth + 1, node_id)

    visit(root, 0)

    fig, ax = plt.subplots(figsize=(max(8, len(graph.nodes()) * 1.2), 5))

    nx.draw_networkx(
        graph,
        pos=positions,
        labels=labels,
        ax=ax,
        node_color="#F4D58D",
        edgecolors="black",
        node_size=2200,
        font_size=9,
        arrows=False
    )

    ax.set_title(title + " — multiple keys per node")
    ax.axis("off")
    st.pyplot(fig)
    plt.close(fig)


# =========================================================
# 8. SESSION STATE AND PATIENT OPERATIONS
# =========================================================

if "trees" not in st.session_state:
    st.session_state.trees = create_trees()

if "patients" not in st.session_state:
    st.session_state.patients = {}

if "animation_order" not in st.session_state:
    st.session_state.animation_order = []


def add_patient(pid, name):
    trees = st.session_state.trees

    for tree in trees:
        tree.insert(pid)

    st.session_state.patients[pid] = name
    st.session_state.animation_order.append(pid)


def remove_patient(pid):
    for tree in st.session_state.trees:
        tree.delete(pid)

    st.session_state.patients.pop(pid, None)
    st.session_state.animation_order = [
        x for x in st.session_state.animation_order if x != pid
    ]


# =========================================================
# 9. SIDEBAR
# =========================================================

st.sidebar.header("👩‍⚕️ Patient Management")

with st.sidebar.form("insert_patient_form"):
    st.subheader("Register Patient")
    patient_id = st.number_input("Patient ID", min_value=1, step=1)
    patient_name = st.text_input("Patient Name")
    insert_clicked = st.form_submit_button("Insert Patient")

if insert_clicked:
    pid = int(patient_id)
    name = patient_name.strip()

    if not name:
        st.sidebar.error("Please enter a patient name.")
    elif pid in st.session_state.patients:
        st.sidebar.warning("This patient ID already exists.")
    else:
        add_patient(pid, name)
        st.rerun()

search_id = st.sidebar.number_input(
    "Patient ID to search",
    min_value=1,
    step=1,
    key="search_id"
)

if st.sidebar.button("Search Patient"):
    pid = int(search_id)

    if pid in st.session_state.patients:
        st.sidebar.success(
            f"Found: {st.session_state.patients[pid]} (ID {pid})"
        )
    else:
        st.sidebar.error("Patient not found.")

delete_id = st.sidebar.number_input(
    "Patient ID to delete",
    min_value=1,
    step=1,
    key="delete_id"
)

if st.sidebar.button("Delete Patient"):
    pid = int(delete_id)

    if pid in st.session_state.patients:
        remove_patient(pid)
        st.rerun()
    else:
        st.sidebar.error("Patient ID not found.")


# =========================================================
# 10. SAMPLE DATA AND RESET
# =========================================================

col1, col2 = st.columns(2)

with col1:
    if st.button("Load Sample Patients"):
        st.session_state.trees = create_trees()
        st.session_state.patients = {}
        st.session_state.animation_order = []

        for pid, name in [
            (50, "Aarav"),
            (30, "Diya"),
            (70, "Ishaan"),
            (20, "Meera"),
            (40, "Rohan"),
            (60, "Anaya"),
            (80, "Kabir"),
            (10, "Tara")
        ]:
            add_patient(pid, name)

        st.rerun()

with col2:
    if st.button("Clear All Patients"):
        st.session_state.trees = create_trees()
        st.session_state.patients = {}
        st.session_state.animation_order = []
        st.rerun()


# Refresh references
bst, avl, rb, bt, treap = st.session_state.trees
patients = st.session_state.patients


# =========================================================
# 11. FIVE TREE VISUALIZATIONS
# =========================================================

st.header("🌳 Visualizations of All Five Trees")

tabs = st.tabs([
    "Plain BST",
    "AVL Tree",
    "Red-Black Tree",
    "B-Tree",
    "Treap"
])

with tabs[0]:
    st.caption("A basic binary search tree; it may become unbalanced.")
    draw_binary_tree(bst.root, "Plain BST", patients)

with tabs[1]:
    st.caption("AVL uses rotations to maintain height balance.")
    draw_binary_tree(avl.root, "AVL Tree", patients)

with tabs[2]:
    st.caption("Red nodes and black nodes show the Red-Black Tree colors.")
    draw_binary_tree(rb.root, "Red-Black Tree", patients, rb.NIL)

with tabs[3]:
    st.caption("A B-Tree node can contain multiple patient IDs.")
    draw_btree(bt.root, "B-Tree")

with tabs[4]:
    st.caption("P is the randomized heap priority of each Treap node.")
    draw_binary_tree(treap.root, "Treap", patients, treap=True)


# =========================================================
# 12. STEP-BY-STEP TREE CONSTRUCTION
# =========================================================

st.header("🎬 Watch How the Trees Are Built")

st.write(
    "Move the slider to see the tree reconstructed after each "
    "patient ID is inserted."
)

animation_order = st.session_state.animation_order[:]

if not animation_order:
    st.info("Load sample patients or insert patients to start the animation.")
else:
    tree_choice = st.selectbox(
        "Select a tree to animate",
        ["Plain BST", "AVL Tree", "Red-Black Tree", "B-Tree", "Treap"]
    )

    step = st.slider(
        "Insertion step",
        min_value=0,
        max_value=len(animation_order),
        value=min(1, len(animation_order))
    )

    st.write(f"Showing {step} of {len(animation_order)} insertions.")

    # Reconstruct a fresh tree using the first 'step' IDs.
    # This is a replay of insertion steps, not a timed rotation animation.
    animated_tree = None

    if tree_choice == "Plain BST":
        animated_tree = BST()
    elif tree_choice == "AVL Tree":
        animated_tree = AVL()
    elif tree_choice == "Red-Black Tree":
        animated_tree = RedBlackTree()
    elif tree_choice == "B-Tree":
        animated_tree = BTree()
    else:
        animated_tree = Treap()
        random.seed(42)

    for pid in animation_order[:step]:
        animated_tree.insert(pid)

    if step == 0:
        st.info("The tree is empty before the first insertion.")
    else:
        last_pid = animation_order[step - 1]
        last_name = patients.get(last_pid, "Patient")

        st.success(f"Step {step}: inserted patient {last_name} (ID {last_pid}).")

        if tree_choice == "Plain BST":
            draw_binary_tree(
                animated_tree.root,
                "Plain BST — Construction",
                patients
            )
            st.write("The ID is inserted according to BST ordering.")

        elif tree_choice == "AVL Tree":
            draw_binary_tree(
                animated_tree.root,
                "AVL Tree — Construction",
                patients
            )
            st.write("The tree checks balance factors and applies rotations.")

        elif tree_choice == "Red-Black Tree":
            draw_binary_tree(
                animated_tree.root,
                "Red-Black Tree — Construction",
                patients,
                animated_tree.NIL
            )
            st.write("The tree may recolor nodes or apply rotations.")

        elif tree_choice == "B-Tree":
            draw_btree(animated_tree.root, "B-Tree — Construction")
            st.write("Full nodes split as keys are inserted.")

        else:
            draw_binary_tree(
                animated_tree.root,
                "Treap — Construction",
                patients,
                treap=True
            )
            st.write("BST ordering and heap priorities determine the structure.")

    st.subheader("Insertion Order")

    for index, pid in enumerate(animation_order[:step], start=1):
        st.write(
            f"{index}. ID {pid} — {patients.get(pid, 'Patient')}"
        )

    if step < len(animation_order):
        next_pid = animation_order[step]
        st.info(f"Next patient ID to insert: {next_pid}")
    else:
        st.success("All patients have been inserted into the selected tree.")


# =========================================================
# 13. PATIENT RECORD TABLE
# =========================================================

st.header("📋 Registered Patients")

if patients:
    patient_df = pd.DataFrame([
        {"Patient ID": pid, "Patient Name": name}
        for pid, name in sorted(patients.items())
    ])
    st.dataframe(patient_df, use_container_width=True)
else:
    st.info("No patients registered yet.")


# =========================================================
# 14. HEIGHT COMPARISON
# =========================================================

st.header("📊 Tree Height Comparison")

height_df = pd.DataFrame({
    "Tree": [
        "Plain BST",
        "AVL Tree",
        "Red-Black Tree",
        "B-Tree",
        "Treap"
    ],
    "Height": [
        binary_height(bst.root),
        binary_height(avl.root),
        binary_height(rb.root, rb.NIL),
        btree_height(bt.root),
        binary_height(treap.root)
    ]
})

st.dataframe(height_df, use_container_width=True)

fig, ax = plt.subplots(figsize=(9, 4))
ax.bar(height_df["Tree"], height_df["Height"])
ax.set_title("Height Comparison of Five Trees")
ax.set_ylabel("Height (levels)")
ax.set_xlabel("Tree Type")
plt.xticks(rotation=15)
st.pyplot(fig)
plt.close(fig)


# =========================================================
# 15. TIME COMPLEXITY COMPARISON
# =========================================================

st.header("⏱️ Time Complexity Comparison")

complexity_df = pd.DataFrame({
    "Operation": ["Search", "Insert", "Delete"],
    "Plain BST": ["O(h)", "O(h)", "O(h)"],
    "AVL Tree": ["O(log n)", "O(log n)", "O(log n)"],
    "Red-Black Tree": ["O(log n)", "O(log n)", "O(log n)"],
    "B-Tree": ["O(log n)", "O(log n)", "O(log n)"],
    "Treap": [
        "Expected O(log n)",
        "Expected O(log n)",
        "Expected O(log n)"
    ]
})

st.dataframe(complexity_df, use_container_width=True)

st.caption(
    "h is the height of the Plain BST. Its worst-case operation time "
    "can be O(n). AVL and Red-Black Trees maintain logarithmic height. "
    "Treap bounds are expected with randomized priorities. B-Tree "
    "bounds assume a fixed node degree."
)

st.success("MediQueue is ready with five tree structures!")
