struct Task:
    id: int128
    content: String[100]
    completed: bool


tasks: public(Task[100])
taskCount: public(int128)


@external
def createTask(_content: String[100]):
    assert len(_content) != 0
    self.tasks[self.taskCount] = Task({id: self.taskCount, content: _content, completed: False})
    self.taskCount += 1


@external
def read(id: int128) -> (int128, String[100], bool):
    assert id < self.taskCount
    return (self.tasks[id].id, self.tasks[id].content, self.tasks[id].completed)


@external
def update(id: int128, content: String[100]):
    assert id < self.taskCount
    self.tasks[id].content = content
