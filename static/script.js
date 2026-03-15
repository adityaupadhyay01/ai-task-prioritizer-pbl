function generateTasks(){

    const num = document.getElementById("taskCount").value;
    const container = document.getElementById("tasks");

    const today = new Date().toISOString().split("T")[0];

    container.innerHTML = "";

    for(let i=0;i<num;i++){
        createTaskRow("", "", "Medium");
    }

}

function createTaskRow(task, deadline, importance){

    const container = document.getElementById("tasks");
    const today = new Date().toISOString().split("T")[0];

    const row = document.createElement("div");
    row.className = "task-row";

    row.innerHTML = `

        <input type="text"
        name="task[]"
        value="${task}"
        placeholder="Task Name"
        required>

        <input type="date"
        name="deadline[]"
        value="${deadline}"
        min="${today}"
        class="date-input"
        required>

        <select name="importance[]">

            <option ${importance==="High"?"selected":""}>High</option>
            <option ${importance==="Medium"?"selected":""}>Medium</option>
            <option ${importance==="Low"?"selected":""}>Low</option>

        </select>

        <button type="button"
        class="delete-btn"
        onclick="deleteTask(this)">
        ✕
        </button>

    `;

    container.appendChild(row);

}

function deleteTask(button){

    const row = button.parentElement;
    row.remove();

    saveTasks();

}

function saveTasks(){

    const tasks = [];

    document.querySelectorAll(".task-row").forEach(row => {

        const task = row.querySelector('input[name="task[]"]').value;
        const deadline = row.querySelector('input[name="deadline[]"]').value;
        const importance = row.querySelector('select[name="importance[]"]').value;

        tasks.push({task, deadline, importance});

    });

    localStorage.setItem("tasks", JSON.stringify(tasks));

}

function loadTasks(){

    const stored = localStorage.getItem("tasks");

    if(!stored) return;

    const tasks = JSON.parse(stored);

    tasks.forEach(t => {

        createTaskRow(t.task, t.deadline, t.importance);

    });

}

document.addEventListener("input", function(e){

    if(e.target.closest(".task-row")){
        saveTasks();
    }

});

window.onload = loadTasks;