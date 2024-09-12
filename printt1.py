task={
  "project": {
    "id": "proj001",
    "name": "Alpha Initiative",
    "status": "Active",
    "deadline": "2024-12-31",
    "tasks": [
      {
        "task_id": "task001",
        "name": "Develop API",
        "assignee": "e456",
        "status": "In Progress",
        "priority": "High",
        "subtasks": [
          {
            "subtask_id": "subtask001",
            "name": "Design API schema",
            "status": "Completed"
          },
          {
            "subtask_id": "subtask002",
            "name": "Implement endpoints",
            "status": "In Progress"
          }
        ]
      },
      {
        "task_id": "task002",
        "name": "Create Frontend",
        "assignee": "e789",
        "status": "Not Started",
        "priority": "Medium",
        "subtasks": []
      }
    ],
    "team_members": [
      {
        "id": "e456",
        "name": "Alice Johnson",
        "role": "Backend Developer"
      },
      {
        "id": "e789",
        "name": "Bob Smith",
        "role": "Frontend Developer"
      }
    ],
    "updates": [
      {
        "update_id": "update001",
        "date": "2024-09-10",
        "content": "API schema design completed. Working on implementing endpoints."
      }
    ]
  }
}

print("The project id is : ", task["project"]["id"])

print("The project name is : ",task["project"]["name"])

print("The project status is : ",task["project"]["status"])

print("The team member of 2nd set is : ", task["project"]["team_members"][1]["name"])

print("The id of bob smith is : ", task["project"]["team_members"][1]["id"])

print("The content of the updates are : ", task["project"]["updates"][0]["content"])