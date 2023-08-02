<script>
    import Task from "./Task.svelte";
    import NewTask from "./NewTask.svelte";
    import { createEventDispatcher } from "svelte";

    export let tasks;
    let removeId;

    const dispatch = createEventDispatcher();

    function toggleRemoveModal({detail}){
      document.getElementById("popup-modal").classList.toggle("hidden")
      removeId = detail
    }

    function remove(){
        tasks = tasks.filter(task => task.id != removeId)
        fetch("http://127.0.0.1:8000/tasks/archived/" + removeId,{
            method: 'PUT'
        })
        document.getElementById("popup-modal").classList.toggle("hidden")
    }

    function submit({detail}){
        const token = localStorage.getItem("access_token")
        if(detail.date == undefined){
          fetch("http://127.0.0.1:8000/tasks/?task=" + detail.description,{
            method: 'POST',
            headers: {
            Authorization: `Bearer ${token}`,
            }
          })
        } else {
          fetch("http://127.0.0.1:8000/tasks/?task=" + detail.description + "&date=" + detail.date ,{
            method: 'POST',
            headers: {
            Authorization: `Bearer ${token}`,
            }
          })
        }
        dispatch("reFetch")
    }
  </script>
  
  
  <main>
    <div style="margin:15px">
      <div>

        <div class="modal hidden" id="popup-modal">
          <div tabindex="-1" class="fixed top-0 left-0 right-0 z-50  p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
              <div class="relative w-full max-w-md max-h-full ml-auto mr-auto mt-48 ">
                  <div class="relative bg-white rounded-lg shadow ">
                      <div class="p-6 text-center">
                          <svg class="mx-auto mb-4 text-gray-400 w-12 h-12" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
                          </svg>
                          <h3 class="mb-5 text-lg font-normal text-gray-500 ">Are you sure you want to delete this task?</h3>
                          <button on:click={remove} data-modal-hide="popup-modal" type="button" class="text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center mr-2">
                              Yes, I'm sure
                          </button>
                          <button on:click={toggleRemoveModal} data-modal-hide="popup-modal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 ">No, cancel</button>
                      </div>
                  </div>
              </div>
          </div>
        </div>


        <div class="mb-16 relative overflow-x-auto shadow-md sm:rounded-lg">
          <table class="w-full text-sm text-left text-gray-500">
            <thead class="text-xs text-gray-700 uppercase bg-gray-300">
                <tr>
                    <th scope="col" class="px-6 py-3">
                        Task name
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Due date
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Done date
                    </th>
                    <th scope="col" class="px-6 py-3">
                        <span class="sr-only">Done</span>
                    </th>
                    <th scope="col" class="px-6 py-3">
                      <span class="sr-only">Delete</span>
                  </th>
                </tr>
            </thead>
            <tbody>
            {#each tasks as {task_name, is_done, id, due_date, done_date}, i(id)}
                <Task on:remove={toggleRemoveModal} {task_name} {is_done} {id} {due_date} {done_date} />
            {/each}
            </tbody>
          </table>
        </div>
        <NewTask on:onSubmit={submit}/>
      </div>
    </div>  
  </main>
 