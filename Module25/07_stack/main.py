class Stack:
    """
    Класс, описывающий стек

    Attributes:
        self.stack (list): стек
    """
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def add(self, elem):
        """
        Метод, добавляющий элемент в стек
        :param elem: элемент
        """
        self.stack.append(elem)

    def pop(self):
        """
        Метод, удляющий последний элемент из стека
        :param elem:
        """
        if len(self.stack) == 0:
            return None
        return self.stack.pop()


class TaskManager:
    """
    Класс, описывающий менеджер задач

    Attributes:
        self.task (dict): задача
    """
    def __init__(self):
        self.task = dict()

    def __str__(self):
        info = []
        if self.task:
            for i_prior in sorted(self.task.keys()):
                info.append(f'{str(i_prior)} {self.task[i_prior]}')
        return ' '.join(info)

    def new_task(self, task, prior):
        """
        Метод добавляющий новую задачу в стек

        :param task: задача
        :param prior: приоритет задачи
        """
        if prior not in self.task:
            self.task[prior] = Stack()
        self.task[prior].add(task)


if __name__ == '__main__':
    manager = TaskManager()
    manager.new_task('сделать уборку', 4)
    manager.new_task('помыть посуду', 4)
    manager.new_task('отдохнуть', 1)
    manager.new_task('сдать дз', 2)
    print(manager)
