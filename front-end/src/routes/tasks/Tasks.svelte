<script>
    import Task from "./Task.svelte";
    import NewTask from "./NewTask.svelte";
    export let tasks;


    function remove({detail}){
        tasks = tasks.filter(task => task.id != detail)
        fetch("http://127.0.0.1:8000/tasks/" + detail,{
            method: 'DELETE'
        } )
    }

    function Submit({detail}){
      console.log(detail)
        fetch("http://127.0.0.1:8000/tasks/?task=" + detail.description + "&date=" + detail.date ,{
            method: 'POST'
        })
    }
  </script>
  
  
  <main>
    <div style="margin:15px">
      <h1>List of tasks</h1>
      <div>
        {#each tasks as {description, is_done, id, due_date}, i(id)}
          <Task on:remove={remove} {description} {is_done} {id} {due_date} {i} />
        {/each}
        <NewTask on:onSubmit={Submit}/>
      </div>
    </div>
  </main>
 