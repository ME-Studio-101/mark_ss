document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('#call2assForm, #call2assForm2');
  const enrollModal = document.getElementById('enrollModal');
  const confirmationModal = document.getElementById('confirmationModal');

  forms.forEach(form => {
    form.addEventListener('submit', handleSubmit);
    console.log(`Submit event listener added to ${form.id}`);
  });

  function handleSubmit(event) {
    event.preventDefault();
    console.log('Form submission prevented, handling...');

    const form = event.target;
    const formData = new FormData(form);
    formData.append('form_id', form.id);

    fetch(form.dataset.url, {
      method: 'POST',
      body: formData,
      headers: {'X-Requested-With': 'XMLHttpRequest'}
    })
    .then(response => response.json())
    .then(data => handleFormResponse(data, form))
    .catch(error => {
      console.error('Fetch error:', error);
      alert('Произошла ошибка при отправке формы. Пожалуйста, попробуйте еще раз.');
    });
  }

  function handleFormResponse(data, form) {
    console.log('Response data:', data);
    if (data.status === 'success') {
      const isModalForm = form.closest('.modal') !== null;
      
      if (isModalForm && enrollModal) {
        bootstrap.Modal.getInstance(enrollModal)?.hide();
        console.log('Enroll modal hidden');
      }

      if (confirmationModal) {
        new bootstrap.Modal(confirmationModal).show();
        console.log('Confirmation modal shown');
      } else {
        alert(data.message);
        console.log('Alert shown');
      }

      form.reset();
      console.log('Form reset');
    } else {
      console.log('Form submission failed:', data.message);
      alert(data.message);
    }
  }
});
