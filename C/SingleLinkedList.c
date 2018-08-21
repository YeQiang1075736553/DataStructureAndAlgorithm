#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
#include <stdbool.h> // ����֧��bool

/*************************************************
��ͷ���ĵ�����

˼·��
1��������������ͷ�巨��β�巨
2������
3���ж��Ƿ�Ϊ��
4���󳤶�
5������
6��������
7��ɾ�����

��̻�����
visual studio 2017

���ߣ�
CSDN���ͣ�https://my.csdn.net/yeqiang19910412
Github��https://github.com/YeQiang1075736553

���ڣ�
2018.8.21

��ע��
���ܻ�����һЩbug��ֻ�ܿ����۷���
**************************************************/

typedef struct Node {
	int data; // ������
	struct Node *pNext; // ָ����
}NODE,*PNODE; // NODE�ȼ���struct Node, PNODE�ȼ���struct Node *

//��������
PNODE creat_list_head(int *data,int len); // ͷ�巨��������ͷ���ĵ�����
PNODE creat_list_tail(int *data,int len); // β�巨��������ͷ���ĵ�����
void travel_list(PNODE pHead); // ��������
bool is_empty(PNODE pHead); // �ж������Ƿ�Ϊ��
int length(PNODE pHead); // ������ĳ���
void sort_list(PNODE pHead); // ����
bool insert_list(PNODE pHead, int pos, int val); // ��pHead��ָ�������ĵ�pos�Ľ��ǰ�����½��
bool delete_list(PNODE pHead, int pos, int *pval); // ɾ����pos��Ԫ��

/////////////////////////////////////////////////////////////////////////////////////////////

int main() {
	int data[10] = { 1,3,4,2,6,33,44,55,22,32 };
	int len = sizeof(data) / sizeof(data[0]);
	PNODE pHead = NULL; // ����ͷָ��

	//pHead = creat_list_head(data,len); // ͷ�巨��������ͷ���ĵ�����

	pHead = creat_list_tail(data, len); // β�巨��������ͷ���ĵ�����

	//if(is_empty(pHead)) // �ж������Ƿ�Ϊ��
	//{ 
	//	printf("����Ϊ�գ�\n");
	//}
	//else{
	//	printf("����Ϊ�գ�\n");
	//}

	//int lengthLinkedList = length(pHead); // ������ĳ���
	//printf("%d\n", lengthLinkedList);

	//travel_list(pHead);
	//sort_list(pHead); // ����

	//travel_list(pHead);
	//bool result = insert_list(pHead, 3, 111); // �ڵ�pos�Ľ��ǰ�����½��
	//bool result = insert_list(pHead, -3, 111);
	//bool result = insert_list(pHead, 30, 111);

	//travel_list(pHead); 
	//int delete_value = 0;
	//int result = delete_list(pHead, 3, &delete_value); // ɾ����pos��Ԫ��

	travel_list(pHead);
	system("pause");
	return 0;
}

/////////////////////////////////////////////////////////////////////////////////////////////

PNODE creat_list_head(int *data,int len) 
{
	// ͷ�巨��������ͷ���ĵ�����

	PNODE pHead = (PNODE)malloc(sizeof(NODE)); // �Ƚ���һ����ͷ���ĵ�����
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
	// β�巨��������ͷ���ĵ�����

	PNODE pHead = (PNODE)malloc(sizeof(NODE)); // �Ƚ���һ����ͷ���ĵ�����
	pHead->pNext = NULL;

	PNODE pTail = pHead; // pTailΪָ��β���Ľ��

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
	// ��������

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
	// �ж������Ƿ�Ϊ��
	if (NULL == pHead->pNext)
	{
		return true;
	}
	return false;
} 

/////////////////////////////////////////////////////////////////////////////////////////////

int length(PNODE pHead)
{
	// ������ĳ���
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
	// ����
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
	// ��pHead��ָ�������ĵ�pos�Ľ��ǰ�����½��
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
	// ɾ����pos��Ԫ��
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