// let todoApp = {
//     todos: [],
//     count: 0,
//     ids: [],
//     isDone: [],
//     addTask(task) {
//         this.todos.push(task)
//         this.count++;
//         this.isDone.push(false)
//         this.ids.push(this.count)
//         console.log("Task" + this.count + " added")
//     },
//     deleteTask(id) {
//         if (id in this.ids) {
//             this.todos.splice(id - 1, id)
//             this.ids.splice(id - 1, id)
//             this.isDone.splice(id - 1, id)
//             console.log("Task" + id + " deleted")
//         } else
//             console.log("No tasks available. Please add task first!")
//     },
//     updateTaskText(id, text) {
//         if (this.todos.length >= id) {
//             this.todos[id] = text
//             console.log("Task" + id + " updated")
//         } else
//             console.log("No tasks available. Please add task first!")
//     },
//     updateTaskAsDone(id) {
//         if (this.todos.length >= id) {
//             this.isDone[id - 1] = true
//             console.log("Task" + id + " marked as done!")
//         } else
//             console.log("No tasks available. Please add task first!")
//     },
//     getAllTasks() {
//         if (this.todos.length > 0) {
//             for (let i = 0; i < this.todos.length; i++) {
//                 console.log(`Id:${this.ids[i]} text: ${this.todos[i]}` + " isDone:" + this.isDone[i])
//             }
//         } else
//             console.log("No tasks added!")
//     }
// }
// todoApp.getAllTasks()
// todoApp.deleteTask(1)
// todoApp.updateTaskAsDone(1)
// todoApp.updateTaskText(1, "text 1")
// todoApp.updateTaskText(2, "text 2")
// todoApp.addTask("This is task 1")
// todoApp.addTask("This is task 2")
// todoApp.addTask("This is task 3")
// todoApp.addTask("This is task 4")
// todoApp.updateTaskAsDone(3)
// todoApp.updateTaskText(3, "new task")
// todoApp.deleteTask(3)
// todoApp.getAllTasks()
// todoApp
// todoApp.updateTaskAsDone(1)
// todoApp.getAllTasks()
// todoApp.deleteTask(1)
// todoApp.getAllTasks()

/**
 * comments:
 * add task check not present that text is empty
 * no limit to number of task added.
 * when task is updated check is not present if text is empty
 * updateTaskText : you use id as index of array but when task is updated you use id-1 as index :: wrong logic
 * all task after id are getting deleted.:: wrong logic
 * code structure is good and readable and in accordance to the question
 */

/**
 *
 *
 * curl 'https://api.relevel.com/api/v2/exams/evaluation/04111488-9603-4665-bdc5-aa90d199cadf/set-evaluator/' \
 *   -H 'authority: api.relevel.com' \
 *   -H 'accept: application/json' \
 *   -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
 *   -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU5MzYyOTc1LCJqdGkiOiIzZGNmNTkxNWI3ZTg0Y2ZiODE5N2E3YmRkMDg1NmZlOSIsInVzZXJfaWQiOjEyODYyN30.-UEpP8KcruHVq89lzNDmhx2DdfLGZXuEgpWJF2fyr18' \
 *   -H 'content-type: application/json' \
 *   -H 'origin: https://relevel.com' \
 *   -H 'platform: desktop_web' \
 *   -H 'referer: https://relevel.com/' \
 *   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
 *   -H 'sec-ch-ua-mobile: ?0' \
 *   -H 'sec-ch-ua-platform: "macOS"' \
 *   -H 'sec-fetch-dest: empty' \
 *   -H 'sec-fetch-mode: cors' \
 *   -H 'sec-fetch-site: same-site' \
 *   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
 *   -H 'x-origin-panamera: ocla-85_olx.com.tr' \
 *   --data-raw '{}' \
 *   --compressed
 */
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NTUzNzg4LCJqdGkiOiI1MmQ5ZDRiMzQ1ZGY0MDExOTYyYjEwMWY2MDMxZDA0YyIsInVzZXJfaWQiOjE4MzIzNDR9.4yrgMeVhuR4SDh_sssFYRomF7MH0k_h3iwQHVEY01zc
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU5MzYyOTc1LCJqdGkiOiIzZGNmNTkxNWI3ZTg0Y2ZiODE5N2E3YmRkMDg1NmZlOSIsInVzZXJfaWQiOjEyODYyN30.-UEpP8KcruHVq89lzNDmhx2DdfLGZXuEgpWJF2fyr18
