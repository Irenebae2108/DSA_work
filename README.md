# 🏥 MediQueue – Patient Management Using Tree Data Structures

**MediQueue** is an interactive patient management application built with Python and Streamlit. It demonstrates how different tree data structures can be used to organize, search, insert, and delete patient records efficiently.

The application visualizes five tree structures and compares their heights and time complexities.

## ✨ Features

- ➕ **Insert Patients:** Add patient records using unique patient IDs.
- 🔍 **Search Patients:** Find records using patient IDs.
- 🗑️ **Delete Patients:** Remove patient records.
- 🌳 **Five Tree Structures:** Explore BST, AVL Tree, Red-Black Tree, B-Tree, and Treap.
- 🎞️ **Step-by-Step Animation:** Observe tree construction as records are inserted.
- 📊 **Tree Visualization:** View and compare tree structures.
- 📈 **Performance Comparison:** Explore tree heights and theoretical time complexities.
- 🖥️ **Interactive Dashboard:** Manage records through a Streamlit interface.

## 🌳 Data Structures Implemented

| Data Structure | Description |
|---|---|
| Binary Search Tree (BST) | Organizes values according to BST ordering rules. |
| AVL Tree | Maintains strict balance using rotations. |
| Red-Black Tree | Uses colours and rotations to maintain balance. |
| B-Tree | Stores multiple keys in each node. |
| Treap | Combines BST ordering with randomized heap priorities. |

## 🛠️ Technologies Used

- Python
- Streamlit
- NetworkX
- Matplotlib
- Pandas

## 📁 Project Structure

```text
MediQueue/
│
├── mediqueue_bst_avl_streamlit.py
├── README.md
└── requirements.txt
```

*Make sure the Python filename matches your actual file. The `requirements.txt` file contains the libraries needed to run the application.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/MediQueue.git
```

### 2. Navigate to the project folder

```bash
cd MediQueue
```

### 3. Install the required libraries

```bash
pip install streamlit networkx matplotlib pandas
```

Alternatively, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run mediqueue_bst_avl_streamlit.py
```

The application will open in your browser.

## 📊 Time Complexity

| Tree | Search | Insertion | Deletion |
|---|---|---|---|
| BST | O(log n) average; O(n) worst | O(log n) average; O(n) worst | O(log n) average; O(n) worst |
| AVL Tree | O(log n) | O(log n) | O(log n) |
| Red-Black Tree | O(log n) | O(log n) | O(log n) |
| B-Tree | O(log n) | O(log n) | O(log n) |
| Treap | O(log n) expected | O(log n) expected | O(log n) expected |

*Note: Actual performance depends on the input, tree structure, and implementation. Treap complexities are expected rather than guaranteed worst-case bounds.*

## 🚀 How to Use

1. Launch the application.
2. Add patient records using patient IDs and the available patient details.
3. Select a tree structure to view its organization.
4. Search for or delete patient records.
5. Use the animation slider to observe tree construction.
6. Compare tree heights and theoretical time complexities.

## 🎯 Learning Outcomes

- Understanding tree data structures and their properties.
- Comparing balanced and unbalanced trees.
- Learning how rotations maintain tree balance.
- Visualizing insertion and deletion operations.
- Understanding algorithmic time complexity.
- Applying data structures to a healthcare-related scenario.

## 🔮 Future Enhancements

- Integrate MySQL or SQLite for permanent storage.
- Add patient appointment scheduling.
- Implement authentication and role-based access.
- Animate tree rotations in real time.
- Compare actual execution times on larger datasets.
- Add patient record export functionality.

## ⚠️ Limitations

This project is an educational prototype. It does not currently provide production-grade security or permanent database storage. Avoid entering real or sensitive patient information.

## 👩‍💻 Author

**Vijaya Kerketta**

M.Sc. Artificial Intelligence and Machine Learning

CHRIST (Deemed to be University)

## 📄 License

This project is intended for educational and learning purposes. You may add an appropriate open-source license if you wish to permit reuse and redistribution.
