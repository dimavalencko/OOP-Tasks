#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class BinaryTree {
private:
  struct Node {
    string key;
    string value;
    Node* left;
    Node* right;
    Node(string k, string v) : key(k), value(v), left(nullptr), right(nullptr) {}
  };

  Node* root;

public:
  BinaryTree() { root = nullptr; }

  void add(string key, string value) {
    root = insert(root, key, value);
  }

  Node* insert(Node* root, string key, string value) {
    if (root == nullptr) {
      return new Node(key, value);
    }

    if (key < root->key) {
      root->left = insert(root->left, key, value);
    } 
    else if (key > root->key) {
      root->right = insert(root->right, key, value);
    }

    return root;
  }

  void remove(string key) {
    root = remove(root, key);
  }

  Node* remove(Node* root, string key) {
    if (root == nullptr) {
      return nullptr;
    }

    if (key < root->key) {
      root->left = remove(root->left, key);
    } 
    else if (key > root->key) {
      root->right = remove(root->right, key);
    } 
    else {
      if (root->left == nullptr) {
        Node* temp = root;
        root = root->right;
        delete temp;
      } 
      else if (root->right == nullptr) {
        Node* temp = root;
        root = root->left;
        delete temp;
      } 
      else {
        Node* smallest = findMin(root->right);

        if (smallest->key == key) {
          Node* temp = root;
          root = root->right;
          delete temp;
        } 
        else {
          root->right = remove(root->right, key);
        }
      }
    }

    return root;
  }

  Node* findMin(Node* root) {
    if (root->left == nullptr) {
      return root;
    }

    Node* temp = root;
    root = root->left;
    delete temp;
    return root;
  }

  string search(string key) {
    Node* node = search(root, key);
    if (node == nullptr) {
      return "Элемент не найден";
    } 
    else {
      return node->value;
    }
  }

  Node* search(Node* root, string key) {
    if (root == nullptr || root->key == key) {
      return root;
    }

    if (key < root->key) {
      return search(root->left, key);
    } 
    else {
      return search(root->right, key);
    }
  }

  void inorder() {
    inorder(root);
  }

  void inorder(Node* root) {
    if (root == nullptr) {
      return;
    }

    inorder(root->left);
    cout << root->key << " " << root->value << endl;
    inorder(root->right);
  }
};

int main() {
  BinaryTree tree;
  
  // Пример использования класса
  tree.add("apple", "A");
  tree.add("banana", "B");
  tree.add("cherry", "C");
  tree.add("date", "D");
  tree.add("elderberry", "E");

  cout << "Search result: " << tree.search("cherry") << endl;

  tree.remove("cherry");

  cout << "Search result after deletion: " << tree.search("cherry") << endl;
  system("pause");

  tree.inorder();

  return 0;
}