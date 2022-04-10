import typing


class MyNode:
    """
    Class describing the node
    """
    def __init__(self, data: any = None, next: any = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    """
    A class describing a singly linked list


    head (any): first node in the list
    length (int): list length
    """
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __str__(self) -> str:
        elem = self.head
        res = [str([elem.data])]
        while elem.next is not None:
            elem = elem.next
            res.append(str([elem.data]))
        return f'[{" ".join(res)}]'

    def append(self, data: int) -> None:
        """
        Function to add an element to a node


        :param data: node value to append
        """
        new_nome = MyNode(data)
        if self.head is None:
            self.head = new_nome
            return

        last_elem = self.head
        while last_elem.next:
            last_elem = last_elem.next

        last_elem.next = new_nome
        self.length += 1

    def get(self, index: int) -> None:
        """
        Finding an element by index

        :param index: search element index
        """
        count = 0
        elem = self.head

        while count != index:
            count += 1
            elem = elem.next

        return elem

    def remove(self, index: int) -> None:
        """
        Remove an element by index

        :param index: search element index
        """
        count = 0
        elem = self.head

        if index < 0 or index > self.length:
            raise IndexError

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        while elem is not None:
            if count == index:
                break
            prev = elem
            elem = elem.next
            count += 1

        prev.next = elem.next
        self.length -= 1


if __name__ == '__main__':
    my_list = LinkedList()
    while True:
        choice = int(input('1 - Добавить\n'
                           '2 - Найти по индексу\n'
                           '3 - Удалить по индексу\n'
                           '4 - Распечатать список\n'
                           '5 - Выход\n'
                           'Ввод: '))
        if choice == 1:
            element = int(input('Введите новый элемент: '))
            my_list.append(element)
        elif choice == 2:
            ind = int(input('Введите индекс: '))
            print(my_list.get(index=ind))
        elif choice == 3:
            ind = int(input('Введите индекс: '))
            my_list.remove(index=ind)
        elif choice == 4:
            print(my_list)
        elif choice == 5:
            print('Конец программы')
            break
        else:
            raise KeyError
        print()
