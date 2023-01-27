module Jekyll
    module Drops
      class UrlDrop < Drop
        def author
          @obj.author
        end
      end
    end
  end