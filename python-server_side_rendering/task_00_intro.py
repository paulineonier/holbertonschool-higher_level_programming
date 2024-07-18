import os

def generate_invitations(template, attendees):
    # Vérifier que le modèle est une chaîne de caractères
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Vérifier que les participants sont une liste de dictionnaires
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Vérifier si le modèle est vide
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Vérifier si la liste des participants est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traiter chaque participant
    for index, attendee in enumerate(attendees, start=1):
        # Remplacer les espaces réservés par les valeurs du dictionnaire
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            invitation = invitation.replace(f"{{{key}}}", value if value else "N/A")
        
        # Écrire le modèle traité dans un fichier
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)

    print(f"{len(attendees)} files generated successfully.")
