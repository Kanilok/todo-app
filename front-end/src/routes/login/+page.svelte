<script>
    let username;
    let password;
    let repeated_password;
    let error_message;
    let login_message = "Login"
    let SERWER_URL = "http://127.0.0.1:8000"

    async function logIn(){
        await fetch(SERWER_URL + "/users/login", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
            }).then(response => {
                if(!response.ok){
                    error_message = "Invalid username or password."
                    changeError()
                } else {
                    return response.json()
                }
            }).then(data => {
                localStorage.setItem("access_token", data.access_token)
                document.getElementById("popup-modal").classList.toggle("hidden")
            }).catch(error => {
                console.log(error)
            });
    }

    async function register(){
        if(password == repeated_password){
            await fetch(SERWER_URL + "/users", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    username: username,
                    hashed_password: password
                })
                }).then(response => {
                    if(response.status == 409){
                        error_message = "Username already taken."
                        changeError()
                    }
                    return response.json()
                }).then(() => {
                    login_message = "Registration"
                    logIn()
                }).catch(error => {
                console.log(error)
                });
        } else {
            error_message = "Passwords are not the same."
            changeError()
        }
    }

    function change(){
        const sign_form = document.getElementById("sign-in-form");
        const log_form = document.getElementById("log-in-form");

        sign_form.classList.toggle("hidden");
        log_form.classList.toggle("hidden");
    }

    function changeError(){
        document.getElementById("toast-danger").classList.toggle("hidden");
    }

</script>

<div id="toast-danger" class="hidden flex items-center w-full ml-auto mr-auto mt-8 max-w-xs p-4 text-red-800 bg-white rounded-lg border border-red-600" style="margin-bottom: -2em" role="alert">
    <div class="inline-flex items-center justify-center flex-shrink-0 w-8 h-8 text-red-500 bg-red-100 rounded-lg ">
        <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z"/>
        </svg>
        <span class="sr-only">Error icon</span>
    </div>
    <div class="ml-3 text-md font-normal">{error_message}</div>
    <button on:click={changeError} type="button" class="ml-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8" data-dismiss-target="#toast-danger" aria-label="Close">
        <span class="sr-only">Close</span>
        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
        </svg>
    </button>
</div>

<div class="modal hidden" id="popup-modal">
    <div tabindex="-1" class="fixed top-0 left-0 right-0 z-50  p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative w-full max-w-md max-h-full ml-auto mr-auto mt-48">
            <div class="relative bg-white rounded-lg shadow ">
                <div class="p-6 text-center">
                    <h3 class="mb-5 text-lg font-normal text-gray-500 ">{login_message} successful!</h3>
                    <a href="/tasks" data-modal-hide="popup-modal" class="text-white bg-green-600 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300  font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center mr-2">
                        Go to Tasks
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="w-full max-w-xs mt-16 ml-auto mr-auto">
    <form on:submit={logIn} id="log-in-form" class="bg-white shadow-xl rounded px-8 pt-6 pb-8 mb-4 ">
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
          Username
        </label>
        <input bind:value={username} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline" type="text" placeholder="Username">
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
          Password
        </label>
        <input bind:value={password}  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:shadow-outline" type="password" placeholder="******************">
      </div>
      <div class="flex flex-col items-center ">
        <button class="hover:bg-blue-700 text-blue-700 font-semibold hover:text-white py-2 px-8 border border-blue-700 rounded" type="submit">
          Log In
        </button>
      </div>
      <p class="pt-8">Don't have an account? <button on:click={change} type="button" class="sign-change-form text-blue-700 font-semibold">Register</button></p>
    </form>

    <form on:submit={register} id="sign-in-form" class="hidden bg-white shadow-xl rounded px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
            Username
          </label>
          <input bind:value={username} class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline" type="text" placeholder="Username">
        </div>
        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Password
          </label>
          <input bind:value={password}  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:shadow-outline" type="password" placeholder="******************">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
            Repeat Password
          </label>
          <input bind:value={repeated_password}  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:shadow-outline" type="password" placeholder="******************">
        </div>
        <div class="flex flex-col items-center ">
          <button class="hover:bg-blue-700 text-blue-700 font-semibold hover:text-white py-2 px-8 border border-blue-700 rounded" type="submit">
            Register
          </button>
        </div>
        <p class="pt-8">Go back to: <button on:click={change} type="button" class="log-change-form text-blue-700 font-semibold">Log In</button></p>
      </form>
  </div>