def show_duplicates_and_get_confirmation(duplicate_pairs):
    if not duplicate_pairs:
        print("✅ No duplicate files found.")
        return []

    print("\n🔁 Found duplicate files:")
    confirmed_for_deletion = []

    for i, (original, duplicate) in enumerate(duplicate_pairs, 1):
        print(f"\nGroup {i}:")
        print(f"Original : {original}")
        print(f"Duplicate: {duplicate}")
        answer = input("Delete duplicate? (y/n): ").strip().lower()
        if answer == 'y':
            confirmed_for_deletion.append(duplicate)

    return confirmed_for_deletion
