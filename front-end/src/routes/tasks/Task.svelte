<script>
    import { createEventDispatcher } from "svelte";
    import { editStore } from "../store.js"

    export let SERWER_URL;
    export let task_name;
    export let description;
    export let is_done;
    export let id;
    export let due_date;
    export let done_date;

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

    function edit(){
        editStore.set({task_name:task_name, description:description, due_date:due_date, id:id, is_done:is_done})
    }

    function done(){
        const token = localStorage.getItem("access_token")
        fetch(SERWER_URL + "/tasks/is-done/" + id, {
            method: 'PUT',
            headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json"
                },
            body: JSON.stringify({
                done_on_time: !is_late,
                task_name: task_name
            })
        })
        dispatch("reFetch")
    }

    function toggleDescription(){
        document.getElementById("description"+id).classList.toggle("hidden")
    }
</script>

    <tr class="bg-gray-100 border-b  hover:bg-gray-50 ">
        <th on:click={toggleDescription} class="w-64 px-6 py-4 font-medium text-gray-900 whitespace-nowrap cursor-pointer">
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
        <td class=" py-4 text-center">
            {#if is_done}
                <button class="bg-transparent hover:bg-yellow-600 text-yellow-600 font-semibold hover:text-white py-2 px-4 border border-yellow-600 rounded" type="button" on:click={done}>to do</button>
            {:else}
                <button class="hover:bg-green-700 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-700 rounded" type="button" on:click={done}>done</button>
            {/if}
        </td>
        <td class=" py-4 text-center">
            <button class="hover:bg-red-600 text-red-600 font-semibold hover:text-white py-2 px-4 border border-red-600 rounded" type="button" on:click={remove}>delete</button>
        </td>
        <td class=" py-4 text-center">
            <button class="hover:bg-blue-600 text-blue-600 font-semibold hover:text-white py-2 px-4 border border-blue-600 rounded" type="button" on:click={edit}>edit</button>
        </td>
    </tr>

    
    <tr id="description{id}" class="hidden">
        <td colspan="100">
            {#if description != null}
                <p class="p-2 m-2 w-full">Description: {description}</p>
            {:else}
                <p class="p-2 m-2 w-full">No description</p>
            {/if}
        </td>
    </tr>
   

