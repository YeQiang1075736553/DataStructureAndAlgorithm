#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
#include <stdbool.h> // 用来支持bool

/*************************************************
带头结点的单链表

思路：
1、整表创建，包括头插法和尾插法
2、遍历
3、判断是否为空
4、求长度
5、排序
6、插入结点
7、删除结点

编程环境：
visual studio 2017

作者：
CSDN博客：https://my.csdn.net/yeqiang19910412
Github：https://github.com/YeQiang1075736553

日期：
2018.8.21

备注：
可能还会有一些bug，只能靠积累发现
**************************************************/

typedef struct Node {
	int data; // 数据域
	struct Node *pNext; // 指针域
}NODE,*PNODE; // NODE等价于struct Node, PNODE等价于struct Node *

//函数声明
PNODE creat_list_head(int *data,int len); // 头插法建立带表头结点的单链表
PNODE creat_list_tail(int *data,int len); // 尾插法建立带表头结点的单链表
void travel_list(PNODE pHead); // 遍历链表
bool is_empty(PNODE pHead); // 判断链表是否为空
int length(PNODE pHead); // 求链表的长度
void sort_list(PNODE pHead); // 排序
bool insert_list(PNODE pHead, int pos, int val); // 在pHead所指向的链表的第pos的结点前插入新结点
bool delete_list(PNODE pHead, int pos, int *pval); // 删除第pos个元素

/////////////////////////////////////////////////////////////////////////////////////////////

int main() {
	int data[10] = { 1,3,4,2,6,33,44,55,22,32 };
	int len = sizeof(data) / sizeof(data[0]);
	PNODE pHead = NULL; // 创建头指针

	//pHead = creat_list_head(data,len); // 头插法建立带表头结点的单链表

	pHead = creat_list_tail(data, len); // 尾插法建立带表头结点的单链表

	//if(is_empty(pHead)) // 判断链表是否为空
	//{ 
	//	printf("链表为空！\n");
	//}
	//else{
	//	printf("链表不为空！\n");
	//}

	//int lengthLinkedList = length(pHead); // 求链表的长度
	//printf("%d\n", lengthLinkedList);

	//travel_list(pHead);
	//sort_list(pHead); // 排序

	//travel_list(pHead);
	//bool result = insert_list(pHead, 3, 111); // 在第pos的结点前插入新结点
	//bool result = insert_list(pHead, -3, 111);
	//bool result = insert_list(pHead, 30, 111);

	//travel_list(pHead); 
	//int delete_value = 0;
	//int result = delete_list(pHead, 3, &delete_value); // 删除第pos个元素

	travel_list(pHead);
	system("pause");
	return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////////

PNODE creat_list_head(int *data,int len) 
{
	// 头插法建立带表头结点的单链表

	PNODE pHead = (PNODE)malloc(sizeof(NODE)); // 先建立一个带头结点的单链表
	pHead->pNext = NULL;

	for (int i = 0; i < len; ++i) 
	{
		PNODE pNew = (PNODE)malloc(sizeof(NODE));
		pNew->data = data[i];
		pNew->pNext = pHead->pNext;
		pHead->pNext = pNew;
	}
	return pHead;	 
}

/////////////////////////////////////////////////////////////////////////////////////////////

PNODE creat_list_tail(int *data, int len)
{
	// 尾插法建立带表头结点的单链表

	PNODE pHead = (PNODE)malloc(sizeof(NODE)); // 先建立一个带头结点的单链表
	pHead->pNext = NULL;

	PNODE pTail = pHead; // pTail为指向尾部的结点

	for (int i = 0; i < len; ++i)
	{
		PNODE pNew = (PNODE)malloc(sizeof(NODE));
		pNew->data = data[i];
		pNew->pNext = NULL;
		pTail->pNext = pNew;
		pTail = pNew;
	}
	return pHead;
} 

/////////////////////////////////////////////////////////////////////////////////////////////

void travel_list(PNODE pHead)
{
	// 遍历链表

	PNODE p = pHead->pNext;
	while (p != NULL)
	{
		printf("%d ", p->data);
		p = p->pNext;
	}
	printf("\n");
	return;
}

/////////////////////////////////////////////////////////////////////////////////////////////

bool is_empty(PNODE pHead)
{
	// 判断链表是否为空
	if (NULL == pHead->pNext)
	{
		return true;
	}
	return false;
} 

/////////////////////////////////////////////////////////////////////////////////////////////

int length(PNODE pHead)
{
	// 求链表的长度
	int num = 0;
	PNODE p = pHead->pNext;
	while (p != NULL)
	{
		num += 1;
		p = p->pNext;
	}
	return num;
} 

/////////////////////////////////////////////////////////////////////////////////////////////

void sort_list(PNODE pHead)
{
	// 排序
	int i, j,temp;
	int len = length(pHead);
	PNODE p, q;
	for (i = 0, p = pHead->pNext; i < len - 1; ++i, p = p->pNext)
	{
		for (j = i + 1, q = p->pNext; j < len; ++j, q = q->pNext)
		{
			if (p->data > q->data) 
			{
				temp = q->data;
				q->data = p->data;
				p->data = temp;			
			}
		}
	}
	return;
} 

/////////////////////////////////////////////////////////////////////////////////////////////

bool insert_list(PNODE pHead, int pos, int val) 
{
	// 在pHead所指向的链表的第pos的结点前插入新结点
	int len = length(pHead);
	if (pos <= 0) 
	{
		PNODE pNew = (PNODE)malloc(sizeof(NODE));
		pNew->data = val;
		pNew->pNext = pHead->pNext;
		pHead->pNext = pNew;
	}
	else if (pos >= len)
	{
		PNODE p = pHead->pNext;
		while (p->pNext != NULL)
		{
			p = p->pNext;
		}
		PNODE pNew = (PNODE)malloc(sizeof(NODE));
		pNew->data = val;
		p->pNext = pNew;
		pNew->pNext = NULL;
		
	}
	else 
	{
		PNODE curr = pHead->pNext;
		PNODE pre = curr;

		for (int i = 0; i < pos-1; ++i)
		{
			pre = curr;
			curr = curr->pNext;

		}
		PNODE pNew = (PNODE)malloc(sizeof(NODE));
		pNew->data = val;
		pre->pNext = pNew;
		pNew->pNext = curr;
	}
	return true;
} 

/////////////////////////////////////////////////////////////////////////////////////////////

bool delete_list(PNODE pHead, int pos, int *pval) {
	// 删除第pos个元素
	int len = length(pHead);
	if (pos > 1 && pos < len)
	{
		PNODE curr = pHead->pNext;
		PNODE pre = curr;
		for (int i = 0; i<pos - 1; ++i)
		{
			pre = curr;
			curr = curr->pNext;
		}
		pre->pNext = curr->pNext;
		*pval = curr->data;
		free(curr);
		curr = NULL;
		return true;
	}
	return false;
}