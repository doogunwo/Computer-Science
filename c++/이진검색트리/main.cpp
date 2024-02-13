#include <iostream>
#include <vector>
using namespace std;

// 이진 검색 트리 노드 구조체
struct Node {
    int data;       // 노드의 데이터 값
    Node* left;     // 왼쪽 자식 노드 포인터
    Node* right;    // 오른쪽 자식 노드 포인터

    // 노드 생성자: 데이터 값과 왼쪽/오른쪽 자식 노드를 nullptr로 초기화
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// 이진 검색 트리에 노드 삽입
void insert(Node*& root, int value) {
    // 루트 노드가 nullptr인 경우, 새로운 노드를 생성하여 루트로 지정
    if (root == nullptr) {
        root = new Node(value);
        return;
    }

    // 삽입하려는 값이 현재 노드의 값보다 작은 경우, 왼쪽 서브트리에 삽입
    if (value < root->data) {
        insert(root->left, value);
    } 
    // 삽입하려는 값이 현재 노드의 값보다 크거나 같은 경우, 오른쪽 서브트리에 삽입
    else {
        insert(root->right, value);
    }
}

// 이진 검색 트리 후위 순회
void postOrderTraversal(Node* root) {
    // 현재 노드가 nullptr인 경우, 재귀 탐색 종료
    if (root == nullptr) return;

    // 왼쪽 서브트리를 후위 순회
    postOrderTraversal(root->left);
    // 오른쪽 서브트리를 후위 순회
    postOrderTraversal(root->right);
    // 현재 노드의 값을 출력 (후위 순회이므로 왼쪽, 오른쪽 서브트리를 모두 탐색한 후에 출력)
    cout << root->data << '\n';
}

int main() {
    // 입출력 속도 향상을 위한 코드
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    Node* root = nullptr;
    int num;

    // 입력을 받아 이진 검색 트리 구축
    while (cin >> num) {
        insert(root, num);
    }

    // 후위 순회 결과 출력
    postOrderTraversal(root);

    return 0;
}
