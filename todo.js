// todo.js

// Todo Application Functionality

// Function to retrieve tasks from local storage
function getTasks() {
    return JSON.parse(localStorage.getItem('tasks')) || [];
}

// Function to save tasks to local storage
function saveTasks(tasks) {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Function to create a new task
function createTask(taskName) {
    const tasks = getTasks();
    const newTask = { id: Date.now(), name: taskName, completed: false };
    tasks.push(newTask);
    saveTasks(tasks);
    return newTask;
}

// Function to edit a task
function editTask(taskId, newTaskName) {
    let tasks = getTasks();
    tasks = tasks.map(task => (task.id === taskId ? {...task, name: newTaskName} : task));
    saveTasks(tasks);
}

// Function to delete a task
function deleteTask(taskId) {
    const tasks = getTasks().filter(task => task.id !== taskId);
    saveTasks(tasks);
}

// Function to filter tasks
function filterTasks(filter) {
    const tasks = getTasks();
    switch (filter) {
        case 'completed':  
            return tasks.filter(task => task.completed);
        case 'pending':  
            return tasks.filter(task => !task.completed);
        default:
            return tasks;
    }
}

// Function to toggle task completion
function toggleTaskCompletion(taskId) {
    let tasks = getTasks();
    tasks = tasks.map(task => (task.id === taskId ? {...task, completed: !task.completed} : task));
    saveTasks(tasks);
}