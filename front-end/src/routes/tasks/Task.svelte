<script>
    import { createEventDispatcher } from "svelte";

    export let task_name;
    export let description
    export let is_done;
    export let id;
    export let due_date;
    export let done_date;
    export let SERWER_URL;


    const date = new Date()

    // checking if due_date has already passed
    let is_late = false
    if (due_date != null){
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
    }
    

    
    const dispatch = createEventDispatcher();

    function remove(){
        dispatch("remove", id)
    }

    function done(){
        done_date = date.getFullYear() + "-" + String(date.getMonth()+1).padStart(2,"0") + "-" + date.getDate()
        is_done = !is_done;
        fetch(SERWER_URL + "/tasks/is-done/" + id + "/?is_late=" + is_late, {
            method: 'PUT',
            
        })
    }

    function toggleDescription(){
        document.getElementById("description"+id).classList.toggle("hidden")
    }
</script>

    <tr on:click={toggleDescription} class="bg-gray-100 border-b  hover:bg-gray-50 ">
        <th  class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
            {#if is_done}
                <span style="text-decoration: line-through">{task_name}</span>
            {:else if is_late}
                <span style="color:red">LATE - {task_name}</span>
            {:else}
                <span>{task_name}</span>
            {/if} 
        </th>
        <td class="px-6 py-4">
            {#if due_date != null}
                {due_date}
            {:else}
                ----
            {/if}
        </td>
        <td class="px-6 py-4">
            {#if is_done}
                {done_date}
            {:else}
                ----
            {/if}
        </td>
        <td class="px-6 py-4 text-right">
            {#if is_done}
                <button class="bg-transparent hover:bg-yellow-600 text-yellow-600 font-semibold hover:text-white py-2 px-4 border border-yellow-700 rounded" type="button" on:click={done}>to do</button>
            {:else}
                <button class="hover:bg-green-700 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-700 rounded" type="button" on:click={done}>done</button>
            {/if}
        </td>
        <td class="px-6 py-4 text-right">
            <button class="hover:bg-red-600 text-red-600 font-semibold hover:text-black py-2 px-4 border border-red-600 rounded" type="button" on:click={remove}>delete</button>
        </td>
    </tr>

    {#if description != null}
        <tr id="description{id}" class="hidden">
            <td colspan="100">
                <p class="p-2 m-2 w-full">Description: {description}</p>
            </td>
        </tr>
    {:else}
    <tr id="description{id}" class="hidden">
        <td colspan="100">
            <p class="p-2 m-2 w-full">No description</p>
        </td>
    </tr>
    {/if}

