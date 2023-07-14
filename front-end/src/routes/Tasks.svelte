<script>
    import Task from "./Task.svelte";
    import NewTask from "./NewTask.svelte";
    export let tasks;


    function remove({detail}){
        tasks = tasks.filter(task => task.id != detail)
        fetch("http://127.0.0.1:8000/task/" + detail,{
            method: 'DELETE'
        } )
    }

    function onSubmit({detail}){
        fetch("http://127.0.0.1:8000/task/?task=" + detail,{
            method: 'POST'
        })
    }
  </script>
  
  
  <main>
    <div>
      <h1>List of tasks</h1>
      <div>
        {#each tasks as {description, is_done, id}, i(id)}
          <Task on:remove={remove} {description} {is_done} {id} {i} />
        {/each}
        <NewTask on:onSubmit={onSubmit}/>
      </div>
    </div>
  </main>
  
  
  <style>
    
  </style>