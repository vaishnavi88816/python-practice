from abc import ABC, abstractmethod
from datetime import datetime

# ==========================================
# 1. ABSTRACTION: Unified Base Interface
# ==========================================
class FileSystemItem(ABC):
    def __init__(self, name: str):
        self.name: str = name
        self.created_date: datetime = datetime.now()

    @abstractmethod
    def get_size(self) -> float:
        """Returns size in Kilobytes (KB)."""
        pass

    @abstractmethod
    def get_details(self) -> str:
        """Returns metadata description summary."""
        pass


# ==========================================
# 2. INHERITANCE & ENCAPSULATION: Subclasses
# ==========================================
class PDFDocument(FileSystemItem):
    def __init__(self, name: str, page_count: int):
        super().__init__(name)
        self.page_count: int = page_count  # Encapsulated state

    def get_size(self) -> float:
        # Standard formula: 50 KB per page
        return float(self.page_count * 50)

    def get_details(self) -> str:
        return f"[PDF File] Name: {self.name} | Pages: {self.page_count} | Size: {self.get_size()} KB"


class ImageDocument(FileSystemItem):
    def __init__(self, name: str, width: int, height: int):
        super().__init__(name)
        self.width: int = width
        self.height: int = height

    def get_size(self) -> float:
        # Dynamic calculation based on dimensions
        return float((self.width * self.height * 4) / 1024)

    def get_details(self) -> str:
        return f"[Image File] Name: {self.name} | Resolution: {self.width}x{self.height} | Size: {self.get_size()} KB"


# ==========================================
# 3. POLYMORPHISM: Composite Container (Folder)
# ==========================================
class Folder(FileSystemItem):
    def __init__(self, name: str):
        super().__init__(name)
        # Holds any FileSystemItem (Documents or other Folders)
        self._contents: list[FileSystemItem] = []

    def add_item(self, item: FileSystemItem) -> None:
        self._contents.append(item)
        print(f"➕ Added '{item.name}' to folder '{self.name}'")

    def get_size(self) -> float:
        # Polmorphic call: Calculates size seamlessly across mixed items
        total_size = sum(item.get_size() for item in self._contents)
        return round(total_size, 2)

    def get_details(self) -> str:
        summary = f"\n📁 Folder: {self.name} (Total Items: {len(self._contents)}, Size: {self.get_size()} KB)\n"
        summary += "-" * 50 + "\n"
        for item in self._contents:
            summary += f"  -> {item.get_details()}\n"
        return summary


# ==========================================
# 4. EXECUTION ENGINE (Driver Code)
# ==========================================
if __name__ == "__main__":
    print("--- 🛠️ Initializing System Structure ---")
    
    # Create concrete documents
    resume = PDFDocument("Resume_2026.pdf", page_count=3)
    profile_pic = ImageDocument("Avatar.png", width=1024, height=768)
    e_book = PDFDocument("Python_DeepDive.pdf", page_count=120)

    # Setup directories
    root_dir = Folder("Root_Drive")
    docs_folder = Folder("Documents")
    photos_folder = Folder("Photos")

    # Map relationships dynamically
    docs_folder.add_item(resume)
    docs_folder.add_item(e_book)
    photos_folder.add_item(profile_pic)

    root_dir.add_item(docs_folder)
    root_dir.add_item(photos_folder)

    print("\n--- 📊 Compiling System Metadata Tree ---")
    print(root_dir.get_details())
    
    print("--- ✅ Process Completed Successfully ---")
