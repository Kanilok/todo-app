<script>
    import { createEventDispatcher } from "svelte";

    export let description;
    export let is_done;
    export let id;
    export let due_date;
    export let add_date;
    export let done_date;
    export let i;

    const date = new Date()

    // checking if due_date has already passed
    let is_late = false
    let due_year = due_date.substring(0,4)
    let due_month = due_date.substring(5,7)
    if(due_month.substring(0,1) == 0){due_month = due_month.substring(1,2)}
    let due_day = due_date.substring(8,10)
    if(due_day.substring(0,1) == 0){due_day = due_day.substring(1,2)}
    
    if(due_year < date.getFullYear()){
        is_late = true
    } else if(due_year == date.getFullYear()){
        if(due_month < (date.getMonth() + 1)){
            is_late = true
        } else if(due_month == (date.getMonth() + 1)){
            if(due_day < date.getDate()){
                is_late = true
            }
        }
    }

    
    


    const dispatch = createEventDispatcher();

    function remove(){
        dispatch("remove", id)
    }

    function done(){
        done_date = date.getFullYear() + "-" + String(date.getMonth()+1).padStart(2,"0") + "-" + date.getDate()
        is_done = !is_done;
        fetch("http://127.0.0.1:8000/tasks/is-done/" + id + "/?is_late=" + is_late, {
            method: 'PUT'
        })
    }
</script>


<div style="padding:10px"> 
    <div style="display:inline-block; width:700px">
        <p style="width:20px; display:inline-block"><b>{i+1}.</b></p>
        <p style="display:inline-block; color:#0d6efd"> added: {add_date}</p> |
        {#if is_done && is_late}
            <p style="display:inline-block; color:#ff781f"> done late: {done_date} </p> |
        {:else if is_done}
            <p style="display:inline-block; color:#198754"> done: {done_date} </p> |
        {:else}
            <p style="display:inline-block; color:#dc3545"> due: {due_date} </p> |
        {/if}
        {#if is_done}
            <span style="text-decoration: line-through; display:inline-block">{description}</span>
        {:else if is_late}
            <span style="display:inline-block; color:red"> YOU'RE LATE - {description}</span>
        {:else}
            <span style="display:inline-block">{description}</span>
        {/if} 
    </div>
    {#if is_done}
        <button class="bg-transparent hover:bg-green-700 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-700 rounded" type="button" on:click={done}>to do</button>
        <button class="hover:bg-yellow-500 text-yellow-500 font-semibold hover:text-black py-2 px-4 border border-yellow-500 rounded" type="button" on:click={remove}>archive</button>
    {:else}
        <button class="hover:bg-green-700 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-700 rounded" type="button" on:click={done}>done</button>
        <button class="text-yellow-500 font-semibold py-2 px-4 border border-yellow-500 rounded opacity-50" type="button" on:click={remove} disabled>archive</button>
    {/if}
</div> 