    const copyButtons = document.querySelectorAll('.copy-code');
    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const codeBlock = button.closest('.container').querySelector('pre code');
            const codeText = codeBlock.innerText;
            navigator.clipboard.writeText(codeText).then(() => {
            }).catch(err => {
                console.error('Error copying text: ', err);
            });
        });
    });
  