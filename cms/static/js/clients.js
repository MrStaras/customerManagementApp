document.addEventListener("DOMContentLoaded", function() {

    // --- DOM ELEMENTS ---
    const addModal = document.getElementById("addClientModal");
    const editModal = document.getElementById("editClientModal");
    const deleteModal = document.getElementById("deleteClientModal");

    const editForm = document.getElementById("editForm");
    const deleteForm = document.getElementById("deleteForm");

    const editNameInput = document.getElementById("editName");
    const editContactInput = document.getElementById("editContact");
    const editCompanyInput = document.getElementById("editCompany");

    // --- EXPOSE FUNCTIONS TO HTML ---
    // Because this script is external, we attach these functions to 'window' 
    // so the onclick="..." attributes in your HTML can find them.

    window.openAddModal = function() {
        addModal.style.display = "block";
    }
    window.closeAddModal = function() {
        addModal.style.display = "none";
    }

    window.openEditModal = function(id, name, contact, company) {
        editNameInput.value = name;
        editContactInput.value = contact;
        editCompanyInput.value = company;
        editForm.action = "/clients/edit/" + id;
        editModal.style.display = "block";
    }
    window.closeEditModal = function() {
        editModal.style.display = "none";
    }

    window.openDeleteModal = function(id) {
        deleteForm.action = "/clients/delete/" + id;
        deleteModal.style.display = "block";
    }
    window.closeDeleteModal = function() {
        deleteModal.style.display = "none";
    }

    // --- AUTO-HIDE SUCCESS MESSAGE ---
    const flashMessage = document.getElementById("flashMessage");
    if (flashMessage) {
        // Wait 3 seconds
        setTimeout(function() {
            // Start fading out
            flashMessage.style.opacity = "0";
            
            // Wait 1 second for fade to finish, then remove
            setTimeout(function() {
                flashMessage.remove();
            }, 1000);
        }, 2000);
    }
});