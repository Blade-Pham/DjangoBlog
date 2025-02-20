from ..models import Project


class ProjectRepository:
    @staticmethod
    def get_all():
        return Project.objects.all()
    def get_by_id(id):
        return Project.objects.filter(id=id).first()
    def create(project):
        return Project.objects.create(**project)
    def delete(id):
        return Project.objects.get(id=id).delete()
    def update(project, data):
        for key, value in data.items():
            setattr(project, key, value)
        project.save()
        return project