
async function analyzeTasks(){

    let rawData = document.getElementById("taskInput").value;
    let sortMode = document.getElementById("sortMode").value;

    // ---- Parse Input ----
    let tasks;
    try{
        tasks = JSON.parse(rawData);
    }catch{
        alert("Invalid JSON format!");
        return;
    }

    // ---- Fetch backend analysis ----
    const response = await fetch("http://127.0.0.1:8000/api/tasks/analyze/",{
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify(tasks)
    });

    let rankedTasks = await response.json();


    // ---- Extra client-side sorting ----

    if(sortMode === "fast"){
        rankedTasks.sort((a,b) => a.estimated_hours - b.estimated_hours);
    }

    else if(sortMode === "deadline"){
        rankedTasks.sort((a,b) => {
            if(!a.due_date) return 1;
            if(!b.due_date) return -1;
            return new Date(a.due_date) - new Date(b.due_date);
        });
    }

    // Default = server priority sort


    // ---- Display ----
    displayResults(rankedTasks);
}


function displayResults(tasks){

    let results = document.getElementById("results");
    results.innerHTML = "";

    tasks.forEach(task => {

        let card = document.createElement("div");

        // Priority colors
        let level = "low";
        if(task.score >= 100) level="high";
        else if(task.score >= 60) level="medium";

        card.className = `card ${level}`;

        card.innerHTML = `
            <h3>${task.title}</h3>
            <span class="score">Score: ${task.score}</span>

            <p>Importance: ${task.importance || 5}</p>
            <p>Estimated Hours: ${task.estimated_hours || 1}</p>
            <p>Due: ${task.due_date || "N/A"}</p>
        `;

        results.appendChild(card);
    });
}
