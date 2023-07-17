<nav class="navbar navbar-expand-lg bg-dark bg-body-tertiary" data-bs-theme="dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">TODO-app</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="/tasks">Tasks</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" href="/about">About</a>
          </li>
        </ul>      
        <button class="btn btn-outline-light">Login</button>
      </div>
    </div>
  </nav>

<slot></slot>

<footer class="bg-dark text-light text-center">
    <p class="mt-3">TODO-app &copy ~ Kamil Motyl 2023</p>
</footer>