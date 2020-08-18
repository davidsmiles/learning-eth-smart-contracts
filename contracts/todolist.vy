taskCount: public(int128)

struct Task:
    id: int128
    content: String[100]
    completed: bool


tasks: public(HashMap[int128, Task])


@payable
@external
def createTask(_content: String[100]):
    self.taskCount = self.taskCount + 1
    self.tasks[self.taskCount] = Task({
        id: self.taskCount, content: _content, completed: True
    })
