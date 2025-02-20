from ..repositories.projectRepository import ProjectRepository
from ..repositories.userRepository import UserRepository


class ProjectService:
    @staticmethod
    def list_projects():
        return ProjectRepository.get_all()

    @staticmethod
    def get_project(id):
        return ProjectRepository.get_by_id(id)
    def create_project(project):
        user_id = project.get("user")
        user_instance = UserRepository.get_by_id(user_id)
        if user_instance:
            project["user"] = user_instance
            return ProjectRepository.create(project)
        return None
    def delete_project(id):
        return ProjectRepository.delete(id)
    def update_project(id, data):
        new_project = ProjectRepository.get_by_id(id)
        if new_project:
            return ProjectRepository.update(new_project, data)
        return None