struct Task:
    id: int128
    content: String[100]
    completed: bool


tasks: public(Task[100])
taskCount: public(int128)


@internal
def _createTask(_content: String[100]):
    assert len(_content) != 0
    self.tasks[self.taskCount] = Task(
        {id: self.taskCount, content: _content, completed: False})
    self.taskCount += 1
    

@external
def createTask(_content: String[100]) -> bool:
    self._createTask(_content)
    return True


@external
def read(id: int128) -> (int128, String[100], bool):
    assert id < self.taskCount
    return (self.tasks[id].id, self.tasks[id].content, self.tasks[id].completed)


@external
def markasread(id: int128):
    assert id < self.taskCount
    self.tasks[id].completed = True


@external
def update(id: int128, content: String[100]):
    assert id < self.taskCount
    self.tasks[id].content = content


@external
def delete(id: int128):
    assert id <= self.taskCount

    unit: int128 = id / 10
    ind: int128 = unit * 10

    if id >= ind and id < ind + 10:
        self.tasks[id] = empty(Task)
        
        for i in range(ind, ind + 10):
            if i < id:
                continue
            
            self.tasks[i] = self.tasks[i + 1] 
            self.tasks[i].id -= 1
        
        self.taskCount -= 1
        
