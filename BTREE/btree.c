#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define SIZE 10

struct btree
{
	int value;
	struct btree* left;
	struct btree* right;
};

static void delete_btree(struct btree* node)
{
    if (node != NULL)
    {
        delete_btree(node->left);
        delete_btree(node->right);
        free(node);
    }
}

static struct btree* insert_node(struct btree* root, int value)
{
    if (root == NULL)
    {
        struct btree* new_node = (struct btree*)malloc(sizeof(struct btree));
        if (new_node == NULL)
        {
            return NULL;
        }
        new_node->value = value;
        new_node->left = NULL;
        new_node->right = NULL;
        return new_node;
    }

    if (value < root->value)
    {
        root->left = insert_node(root->left, value);
    }
    else
    {
        root->right = insert_node(root->right, value);
    }
    return root;
}

static int btree_min(struct btree* root)
{
    if (root == NULL)
    {
        return NULL;
    }
    int min = root->value;
    while (root->left != NULL)
    {
        root = root->left;
        min = root->value;
    }
    return min;
}

static int btree_max(struct btree* root)
{
    if (root == NULL)
    {
        return NULL;
    }
    int max = root->value;
    while (root->right != NULL)
    {
        root = root->right;
        max = root->value;
    }
    return max;
}

static bool node_exists(struct btree* root, int value)
{
    if (root == NULL)
    {
        return false;
    }
    while (root != NULL)
    {
        if (root->value == value)
        {
            return true;
        }
        else if (value < root->value)
        {
            root = root->left;
        }
        else
        {
            root = root->right;
        }
    }
    return false;
}



int main()
{
    // tablica SIZE pseudolosowych liczb ca³kowitych
    int* array = (int*)malloc(SIZE * sizeof(int));
    if (!array)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }

    srand((unsigned int)time(NULL));
    for (size_t i = 0; i < SIZE; i++)
    {
        array[i] = rand()%100;
    }

    // tablica 100 pseudolosowych liczb ca³kowitych
    //int array[100] = {974, -1105, 426, -270, 66, 582, 347, -191, -1184, 172, -280, 693, -1180, 953, -284, 83, -135, 1056, 1033, 590, 611, 488, 1060, 498, 907, -130, 375, -436, 509, -964, 972, 368, 616, 918, -34, 421, -1169, 825, -419, 1171, -942, -351, -256, 430, -13, 10, 1014, 120, -177, 814, 659, -858, 891, 1129, -1067, 636, -918, 850, 1119, -765, 772, 262, 823, 812, 107, -1170, 833, 1192, 170, 379, 470, -115, 1002, 613, 166, 1161, 774, -979, -739, -747, -104, -457, 786, 367, -300, -610, 682, -1021, 95, 33, 524, -137, -743, 1037, 96, 934, 15, -1100, -421, 522};

    // drzewo binarne
    struct btree* root = NULL;

    // algorytm wstawiania elementów do drzewa
    for (size_t i = 0; i < SIZE; i++)
    {
        if (node_exists(root, array[i]) != true)
        {
            root = insert_node(root, array[i]);
            if (root == NULL)
            {
                printf("Memory allocation failed.\n");
                free(array);
                return 1;
            }
        }
    }

    free(array);

    printf("Wartosc minimalna: %d\n", btree_min(root));
    printf("Wartosc maksymalna: %d\n", btree_max(root));
    printf("Czy istnieje w tablicy [ %d ]: %d\n", 1037, node_exists(root, 1037));
    printf("Czy istnieje w tablicy [ %d ]: %d\n", 929, node_exists(root, 929));


    delete_btree(root);
	return 0;
}