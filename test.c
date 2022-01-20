#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isValidExp(char *);
bool isOperator(char);
bool isOperand(char);

int value(char c) { return (c - '0'); }

int evaluate(char *exp)
{
    if (*exp == '\0')
        return -1;

    int res = value(exp[0]);

    for (int i = 1; exp[i]; i += 2)
    {

        char opr = exp[i], opd = exp[i + 1];

        if (!isOperand(opd))
            return -1;

        if (opr == '+')
            res += value(opd);
        else if (opr == '-')
            res -= value(opd);
        else if (opr == '*')
            res *= value(opd);
        else if (opr == '/')
            res /= value(opd);

        else
            return -1;
    }
    return res;
}

int main()
{
    system("cls");
    char exp[100];
    printf("> ");
    fgets(exp, sizeof(exp), stdin);
    puts(exp);
    if (isValidExp(exp))
        printf("Valid expression\n");
    else
        printf("Invalid expression\n");

    char exp1[100];

    for (int k = 0, l = 0; k < 100; k += 2, l++)
    {
        exp1[l] = exp[k];
    }

    int res = evaluate(exp1);
    (res == -1) ? printf("") : printf("Value of %s is %d", exp1, res);
}

bool isValidExp(char *exp)
{
    int length = strlen(exp);
    int i;

    for (i = 0; i < length; i = i + 4)
    {
        if (!isOperand(exp[i]))
            return false;
    }

    for (i = 2; i < length; i = i + 4)
    {
        if (!isOperator(exp[i]))
            return false;
    }
    return true;
}

bool isOperator(char ch)
{
    if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
        return true;
    return false;
}

bool isOperand(char ch)
{
    if (ch > '0' && ch < '9')
        return true;
    return false;
}