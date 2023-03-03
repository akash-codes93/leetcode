class Task {
    constructor(taskName, taskId) {
        this.taskId = taskId
        this.taskName = taskName;
        this.isComplete = false;
    }
}


class ToDo {
    MAX_TASK = 10

    constructor() {
        this.activeTaskCount = 0;
        this.taskMap = new Map();
        this.maxTaskId = 0
    }

    addTask(taskName) {
        if (taskName == null || taskName === "") {
            console.log("Please send a valid task name")
        } else if (this.activeTaskCount >= this.MAX_TASK) {
            console.log("Task list is full, please complete few/delete tasks")
        } else {
            this.taskMap.set(this.maxTaskId, new Task(taskName, this.maxTaskId));
            console.log(`Task added successfully. taskId: ${this.maxTaskId}, taskName: ${taskName}`)
            this.activeTaskCount++;
            this.maxTaskId++;
        }
    }

    checkTaskExists(taskId){
        return this.taskMap.has(taskId);

    }

    checkTaskCompleted(taskId){
        return this.taskMap.get(taskId).isComplete;
    }

    deleteTask(taskId){
        if(!this.checkTaskExists(taskId)){
            console.log("Task not present!")
        }
        else{
            if(!this.checkTaskCompleted(taskId)){
                this.activeTaskCount --;
            }
            this.taskMap.delete(taskId);
            console.log("Task deleted successfully")
        }
    }

    updateTaskName(taskId, taskName){
        if(!this.checkTaskExists(taskId)){
            console.log("Task not present!")
        }
        else {
            let task = this.taskMap.get(taskId)
            task.taskName = taskName;
            console.log(`Task updated successfully. taskId: ${this.maxTaskId}, taskName: ${taskName}`)
        }
    }

    updateTaskComplete(taskId){
        if(!this.checkTaskExists(taskId)){
            console.log("Task not present!")
        }
        else if(this.checkTaskCompleted(taskId)){
            console.log("Task is already complete")
        }
        else {
            let task = this.taskMap.get(taskId)
            task.isComplete = true;
            this.activeTaskCount --;
            console.log("Task completed successfully")
        }
    }

    getAllTask(){
        if(this.taskMap.size <= 0){
            console.log("No task present")
        }
        else{
            console.log("##############################################");
            this.taskMap.forEach((value, key, map) =>{
                console.log(`TaskId: ${key}, TaskName: ${value.taskName}, Completed: ${value.isComplete}`);
            })
            console.log("##############################################");
        }
    }
}


let todoApp = new ToDo()
todoApp.addTask("Get hair cut")
todoApp.addTask("Solve leet-code question")
todoApp.updateTaskComplete(0)
todoApp.addTask("Take protein")
todoApp.deleteTask(1)
todoApp.updateTaskName(2, "Take protein shake")
todoApp.updateTaskComplete(2)
todoApp.getAllTask()
